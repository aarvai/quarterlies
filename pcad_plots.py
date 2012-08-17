import numpy as np
from matplotlib import pyplot as pp

from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime
from Chandra import Time

import filter_times as bad
from utilities import smaller_axes


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

def pointing_stab(error_axis, start, stop, savefig=True):  #NOT DONE YET!  NEEDS 95%
    # Identify msid corresponding to attitude error in selected axis
    i = ['roll', 'pitch','yaw'].index(error_axis.lower()) 
    msid = 'aoatter' + str(i + 1)
    print error_axis
    print msid
    # Fetch data and interpolate to 10 second samples
    data = fetch.Msid(msid, start, stop)
    data.interpolate(dt=10)
    t = data.times
    err = data.vals
    # Reshape with a new column for each 24 hour period 
    err_by_day = err[:-np.mod(len(err),8640)].reshape((8640, np.floor(len(err) / 8640.)))
    # Select a timestamp in the middle of the 24 hour period to represent the day
    t_rep = t[4319::8640][:err_by_day.shape[1]]
    # Compute standard dev for each day
    point_stab = np.std(err_by_day, 1)
    # Plot results
    plot_cxctime(t_rep, point_stab)
    pp.title(error_axis.upper() + ' POINTING STABILITY')
    pp.ylabel('deg')
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
    npm_2minbuffer = npm & np.append(np.zeros(4, dtype=bool), npm[4:]) 
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
    start_i = np.nonzero([(dates[i][:7] == Time.DateTime(start).iso[:7]) for i in range(len(dates))])
    stop_i = np.nonzero([(dates[i][:7] == Time.DateTime(stop).iso[:7]) for i in range(len(dates))])
    dates = dates[start_i[0]:stop_i[0] + 2] 
    
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
        ax2, ax_pos, ax_width, ax_height = smaller_axes(ax1)
        # Place datapoint on the 15th of the month (14 days = 1209600 sec)
        plot_cxctime(np.array(Time.DateTime(dates[:-1]).secs) + 1209600, 
                     slopes[:,rw - 1], 'k-d')
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

    
    
##-------------------------------------------------------------
# TO ADD LATER:
##-------------------------------------------------------------
# Pointing Control and Stability
#temp=LTTquery([ltt_root 'A_PNT_CTRL_STAB.ltt'],time(1999275),tstop,'keep dat');
#plot_ltt(temp,2)
# PITCH_CTRL, MEAN PITCH POINTING CONTROL, ARCSEC, MEAN - added in ltt, but check
# YAW_CTRL, MEAN YAW POINTING CONTROL, ARCSEC, MEAN - added in ltt, but check
# PITCH_STAB, PITCH_STAB, ARCSEC, MEAN - above, but not done yet
# YAW_STAB, YAW_STAB, ARCSEC, MEAN - above, but not done yet

# Add table calcs and SA angle ranges - perhaps in a text report?