import numpy as np
from matplotlib import pyplot as pp

from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime
from Chandra import Time

import filter_times as bad
from utilities import smaller_axes, reshape_array


##-----------------------------------------------------
# PCAD Plotting Functions

def fss(start, stop, savefig=True):
    data = fetch.Msidset(['aoalpang', 'aobetang', 'dp_fss_css_angle_diff', 
                         'dp_pitch', 'aosunprs'], start=start, stop=stop, 
                          stat='5min')
    data.filter_bad_times(table=getattr(bad, 'bad_all'))
    data.interpolate(dt=300)
    ok = (data['dp_pitch'].vals < 135) & (data['aosunprs'].vals == 'SUN ') 
    zipvals = zip([1, 2, 3], ['aoalpang', 'aobetang', 'dp_fss_css_angle_diff'],
                  ['FSS Roll Angle - AOALPANG', 'FSS Pitch Angle - AOBETANG', 
                   'FSS / CSS Sun Vector Difference'])
    pp.figure(figsize=(8, 12))
    for subplot, msid, title in zipvals:
        pp.subplot(3, 1, subplot)
        plot_cxctime(data[msid].times[ok], data[msid].vals[ok])
        pp.title(title)
        pp.ylabel('deg')
        pp.grid()
        ax = pp.gca()
        pp.setp(ax.get_xticklabels(), 'rotation', 0)
    if savefig==True:
        pp.savefig('fss_angles.png')
        pp.close()        

def pointing_stab(error_axis, start, stop, savefig=True):  #NOT DONE YET!  Doesn't match expected results
    
    # Identify msid corresponding to attitude error in selected axis
    i = ['roll', 'pitch','yaw'].index(error_axis.lower()) 
    msid = 'aoatter' + str(i + 1)
    
    # Fetch data and interpolate to 10 second samples
    data = fetch.Msidset([msid, 'aopcadmd', 'aofunlst', 'aoacaseq'], start, stop)
    data.interpolate(dt=1.0)
    t = data[msid].times
    err = data[msid].vals * 180 / np.pi * 3600 # conv rad to arcsec
    # Reshape with a new column for each 10.0 sec period
    err_by_10sec = reshape_array(err, 10)
    # Compute a standard deviation for each period
    stdev = np.std(err_by_10sec, axis=0)
    # Reshape with a new column for each day
    stdev_by_day = reshape_array(stdev, 8640)
    
    # Create filter for NPM, Kalman (+180 sec), and no momentum dumps (+900 sec)
    npm = (data['aopcadmd'].vals == 'NPNT')
    kalm = (data['aoacaseq'].vals == 'KALM')
    kalm_3min = np.append(np.zeros(180, dtype=bool), kalm[180:]) 
    no_dump = (data['aofunlst'].vals == 'NONE')
    no_dump_15min = np.append(np.zeros(900, dtype=bool), no_dump[900:]) 
    ok = npm & kalm & kalm_3min & no_dump & no_dump_15min
    # Reshape with a new column for each 10.0 sec period
    ok_by_10sec = reshape_array(ok, 10)
    # Compute a filter for each 10.0 sec period
    ok_10sec = multiply.reduce(ok_by_10sec, axis=0)
    # Reshape with a new column for each day
    ok_by_day = reshape_array(ok_10sec, 8640)
    
    # Compute 95th percentile for each daily set of standard deviations, only including "ok" points
    point_stab = [np.percentile(stdev_by_day[:,i][ok_by_day[:,i]], 95) for i in range(ok_by_day.shape[1])]
    
    # Select a timestamp in the middle of the 24 hour period to represent the day
    t_rep = t[4319::8640][:ok_by_day.shape[1]]
    # Plot results
    plot_cxctime(t_rep, point_stab)
    pp.title(error_axis.upper() + ' POINTING STABILITY')
    pp.ylabel('arcsec')
    if savefig == True:
        pp.savefig(error_axis.lower() + '_pointing_stab.png')
        pp.close()

def drag_torque(start, stop, dt=328, verbose=False, plot_months=True, savefig=True):  
    msids = ['aofunlst', 'aopcadmd', 'coradmen', 
             'aorwcmd1', 'aorwcmd2', 'aorwcmd3', 
             'aorwcmd4', 'aorwcmd5', 'aorwcmd6', 
             'aorwspd1', 'aorwspd2', 'aorwspd3',
             'aorwspd4', 'aorwspd5', 'aorwspd6']
    # Collect Data
    data = fetch.MSIDset(msids, start, stop)
    data.interpolate(dt=dt, filter_bad=False)
    data.filter_bad_times(table=getattr(bad, 'bad_all'))
    
    # Filter for NPM (+2 min buffer), No dumps, and Rad Mon Enabled
    npm = (data['aopcadmd'].vals == 'NPNT')
    i_2min = np.ceil(120.0 / dt)
    npm_2minbuffer = npm & np.append(np.zeros(i_2min, dtype=bool), npm[i_2min:]) 
    ok = ((data['aofunlst'].vals == 'NONE') & 
          (data['coradmen'].vals == 'ENAB') & npm_2minbuffer)    
    
    # Determine the logical-or of bad values for all MSIDs and use this
    # to further filter the data sample
    nvals = np.sum(ok)
    bads = np.zeros(nvals, dtype=bool)
    for msid in data.values():
        if verbose == True:
            print msid.msid, np.sum(msid.bads[ok])
        bads = bads | msid.bads[ok]
    ok[ok] = ok[ok] & ~bads
    
    # Generate month boundaries
    start_year = Time.DateTime(start).iso[:4]
    end_year = Time.DateTime(stop).iso[:4]
    years = np.arange(int(start_year), int(end_year) + 1)
    months = np.arange(1, 13)
    dates = [str(year) + '-' + str(month).zfill(2) + '-01 00:00:00.00' 
            for year in years for month in months]
    dates.append(str(int(end_year) + 1) + '-01-01 00:00:00.00')
    i_start = np.nonzero([(dates[i][:7] == Time.DateTime(start).iso[:7]) for i in range(len(dates))])
    i_stop = np.nonzero([(dates[i][:7] == Time.DateTime(stop).iso[:7]) for i in range(len(dates))])
    dates = dates[i_start[0]:i_stop[0] + 2] 
    
    # Compute slopes for each month
    slopes = np.empty((len(dates) - 1, 6))
    sf = 60 / (2 * np.pi)
    for i in np.arange(len(dates) - 1):
        in_range = ((data['aofunlst'].times > Time.DateTime(dates[i]).secs) & 
                    (data['aofunlst'].times < Time.DateTime(dates[i+1]).secs))
        for rw in np.arange(1,7):
            poly = np.polyfit(data['aorwspd' + str(rw)].vals[ok & in_range] * sf, 
                              data['aorwcmd' + str(rw)].vals[ok & in_range], 1)
            slopes[i, rw - 1] = poly[0]  
            # Plot monthly data and slope 
            if plot_months == True:
                pp.figure()
                pp.plot(data['aorwspd' + str(rw)].vals[ok & in_range] * sf, 
                     data['aorwcmd' + str(rw)].vals[ok & in_range], 'k.')
                pv = np.polyval(poly, data['aorwspd' + str(rw)].vals[ok & in_range] * sf)
                pp.plot(data['aorwspd' + str(rw)].vals[ok & in_range] * sf, pv, 'g')
                pp.ylabel('Commanded Torque [ft-lbf] - AORWCMD' + str(rw))
                pp.xlabel('Speed [RPM] - AORWSPD' + str(rw))
                pp.title(dates[i][:10] + ', RW' + str(rw))
                pp.savefig('RW' + str(rw) + ' ' + dates[i][:10] + '.png')  
                if (rw == 1) or (rw == 3) or (rw == 5):
                    pp.xlim([0,4500])
                else:
                    pp.xlim([-4500, 0])
                pp.grid()
                pp.close()
    
    # Plot results
    pp.figure(figsize=(8, 12))
    for rw in np.arange(1, 7):
        ax1 = pp.subplot(6, 1, rw)
        ax2 = smaller_axes(ax1)
        # Place datapoint on the 15th of the month (14 days = 1209600 sec)
        plot_cxctime(np.array(Time.DateTime(dates[:-1]).secs) + 1209600, 
                     slopes[:,rw - 1], 'k.', ms=3)
        pp.ylim([.4e-6, 2e-6])
        ax2.yaxis.set_ticks([0.4e-6, .8e-6, 1.2e-6, 1.6e-6, 2e-6])
        pp.setp(ax2.get_xticklabels(), 'rotation', 0)
        if rw == 1:
            pp.title('Drag Torque Analysis \n RW1')            
        else:
            pp.title('RW' + str(rw))
        if rw == 3:
            pp.ylabel('Slope of Commanded Torque vs Observed Wheel Speed                   ')
    if savefig == True:
        pp.savefig('Drag_Torque_Slopes.png')
        pp.close()
    return slopes, dates

def cmd_vs_act_torque(start, stop, savefig=True):   #NOT TESTED YET!
    msids = ['awd1tqi', 'awd2tqi', 'awd3tqi', 
             'awd4tqi', 'awd5tqi', 'awd6tqi', 
             'aorwcmd1', 'aorwcmd2', 'aorwcmd3', 
             'aorwcmd4', 'aorwcmd5', 'aorwcmd6']
    data = fetch.Msidset(msids, start, stop, stat='5min')
    conv = 0.042 * 0.737562149277 # (N-m / A) * (ft-lbf / N-m)
    # Compute actual minus commanded torque
    rw1 = data['awd1tqi'].vals * conv - data['aorwcmd1'].vals # ft-lbf
    rw2 = data['awd2tqi'].vals * conv -	data['aorwcmd2'].vals
    rw3 = data['awd3tqi'].vals * conv -	data['aorwcmd3'].vals
    rw4 = data['awd4tqi'].vals * conv -	data['aorwcmd4'].vals
    rw5 = data['awd5tqi'].vals * conv -	data['aorwcmd5'].vals
    rw6 = data['awd6tqi'].vals * conv -	data['aorwcmd6'].vals
    rw = [rw1, rw2, rw3, rw4, rw5, rw6] 
    # Plot results
    for i in arange(1, 6):
        subplot(6, 1, i)
        plot_cxctime(data.times, rw[i])
        title('RW Actual minus Commanded Torque')
        ylabel('ft-lbf')
    if savefig == True:
        pp.savefig('RW_Act_Minus_Cmd_Torque.png')
        pp.close()

def collect_bias_data(t_stop):
    msids = ['4rt707t','4rt708t','airu2bt','airu2g1i','airu2g1t','airu2g2i',
             'airu2g2t','airu2vft','aogbias1','aogbias2','aogbias3',
             'aokalstr','aomanend','aonstars','aosares1','aorwspd1',
             'aorwspd2','aorwspd3','aorwspd4','aorwspd5','aorwspd6',
             'aosymom1','aosymom2','aosymom3','Dist_SatEarth','oobthr62',
             'tcylaft6']
    biases=fetch.MSIDset(msids,'2003:201',t_stop,stat='5min') 
    biases.write_zip('biases.zip')    
    
##-------------------------------------------------------------
# TO ADD LATER:
##-------------------------------------------------------------
# Pointing Control and Stability
#temp=LTTquery([ltt_root 'A_PNT_CTRL_STAB.ltt'],time(1999275),tstop,'keep dat');
#plot_ltt(temp,2)
# PITCH_STAB, PITCH_STAB, ARCSEC, MEAN - above, but not done yet
# YAW_STAB, YAW_STAB, ARCSEC, MEAN - above, but not done yet

# Add table calcs and SA angle ranges - perhaps in a text report?