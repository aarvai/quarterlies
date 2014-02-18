import numpy as np
from matplotlib import pyplot as pp

from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime
from Chandra.Time import DateTime
from kadi import events

from utilities import append_to_array, find_first_after, same_limits, heat_map, count_by_month, sum_by_month, mean_by_month


#-------------------------------------------------------------
# MUPS Tank Pressure Update Plot

def mups_tank(stop):
    x=fetch.Msidset(['pmtank1t', 'pmtank2t', 'pmtank3t', 'pmfp01t', 'pmtankp',
                     'aosares1', 'aosares2'], '2009:100:00:00:00.000', stop,
                     stat='5min')
    pmtankt = np.mean([x['pmtank1t'].means, x['pmtank2t'].means, 
                       x['pmtank3t'].means], axis=0)                 
    aosares = np.mean([x['aosares1'].means, x['aosares2'].means], axis=0)      
    pp.figure()
    pp.subplot(4,1,1)
    plot_cxctime(x['pmtank1t'].times,pmtankt)
    pp.title('Average Tank Temperature')
    pp.ylabel('deg F')
    pp.subplot(4,1,2)
    plot_cxctime(x['pmfp01t'].times,x['pmfp01t'].vals)
    pp.title('MUPS Fill Panel Temperature')
    pp.ylabel('deg F')
    pp.subplot(4,1,3)
    plot_cxctime(x['pmtankp'].times,x['pmtankp'].vals)
    pp.title('MUPS Tank Pressure')
    pp.ylabel('psia')
    pp.subplot(4,1,4)
    plot_cxctime(x['aosares1'].times,aosares)
    pp.title('Average Solar Array Angle')
    pp.ylabel('deg')
    pp.tight_layout()
    pp.savefig('TankPressureUpdate.png')

#-------------------------------------------------------------
# Temperatures of Thermistors with Dropouts Plot

def therm_dropouts(stop):
    vars=['plaev2bt','pm1thv1t','pm2thv1t','pm2thv2t','pr1tv01t']
    col = ['b','g','r','c','m']
    ys=np.array([[40,220],[90,180],[80,200],[90,180],[80,180]])
    x = fetch.Msidset(vars,'2004:001', stop, stat='daily')
    pp.figure(figsize=(8,12))
    for i in range(len(vars)):
        pp.subplot(5,1,i+1)
        plot_cxctime(x[vars[i]].times, x[vars[i]].maxes, col[i])
        pp.title(x[vars[i]].msid.upper() + ' Maximum Daily Temperature')
        pp.ylabel(x[vars[i]].unit)
        pp.ylim(ys[i])
    pp.savefig('DropoutThermistorTemps.png')


##-------------------------------------------------------------
# Heater Duty Cycle Plots

def htr_dc(msid, **kwargs):
    """Generate plots related to the heater cycle trending of a given MSID and
    save them to the current working directory.
    
    Input:
    :var:  MSID or derived parameter name (string)
    
    Optional inputs:
    :tstart:        Start time (default is 2000:001)
    :tstop:         Stop time (default is None)
    :on_temp:      A temperature near the bottom of the heater band 
                   (default is min temp + five)
    :off_temp:     A tempeature near the top of the heater band
                   (default is max temp - five)
    
    e.g.
    plot_htr_dc('PM3THV2T', start='2005:001', stop='2014:001', on_temp=50, off_temp=89)   
    """
    tstart = kwargs.pop('tstart', '2000:001')
    tstop = kwargs.pop('tstop', None)

    temp = fetch.Msid(msid, tstart, tstop)
    
    temp.plot()
    
    on_temp = kwargs.pop('on_temp', min(temp.vals) + 5)
    off_temp = kwargs.pop('off_temp', max(temp.vals) - 5) 
    
    dt = diff(temp.vals)
    
    local_min = (append_to_array(dt <= 0., pos=0, val=bool(0)) & 
                 append_to_array(dt > 0., pos=-1, val=bool(0)))
    local_max = (append_to_array(dt >= 0., pos=0, val=bool(0)) & 
                 append_to_array(dt < 0., pos=-1, val=bool(0)))
    
    htr_on_range = temp.vals < on_temp
    htr_off_range = temp.vals > off_temp
    
    htr_on = local_min & htr_on_range
    htr_off = local_max & htr_off_range
    
    #remove any incomplete heater cycles at end of timeframe
    last_off = nonzero(htr_off)[0][-1]
    htr_on[last_off:] = 0
    
    t_on = temp.times[htr_on]
    t_off = temp.times[htr_off]
    
    match_i = find_first_after(t_on, t_off)
    
    dur = t_off[match_i] - t_on
    
    #compute duty cycles by month
    dates, on_freq = count_by_month(t_on)
    dates, on_time = sum_by_month(t_on, dur)
    dates, avg_on_time = mean_by_month(t_on, dur)
    len_mo = 365.25/12*24*3600
    firstofmonth = [DateTime(DateTime(date).iso[:7] + '-01 00:00:00.00').secs for date in dates]
    firstofmonth.append(DateTime(DateTime(dates[-1] + len_mo).iso[:7] + '-01 00:00:00.00').secs)
    month_dur = diff(firstofmonth)
    dc = on_time / month_dur
       
    figure(1)
    plot_cxctime(t_on, dur, 'b.', alpha=.05, mew=0)
    pp.ylabel('On-Time Durations [sec]')
    pp.title('MUPS-3 Valve Heater On-Time Durations')
    pp.savefig(msid+'_htr_ontime.png')    
    
    figure(2)
    plot_cxctime(temp.times, temp.vals, mew=0)
    plot_cxctime(temp.times, temp.vals, 'b*',mew=0)
    plot_cxctime(temp.times[htr_on], temp.vals[htr_on], 'c*',mew=0, label='Heater On')
    plot_cxctime(temp.times[htr_off], temp.vals[htr_off], 'r*',mew=0, label='Heater Off')
    pp.legend()
    pp.savefig(msid+'_htr_on_off_times.png')
    
    figure(3) 
    pp.hist(dur, bins=100, normed=True)
    pp.xlabel('On-Time Durations [sec]')
    pp.title('MUPS-3 Valve Heater On-Time Durations')
    pp.savefig(msid+'_htr_ontime_dur.png')    
    
    figure(4) 
    plot_cxctime(dates, dc*100, '*', mew=0)
    plot_cxctime(dates, dc*100)
    pp.title('MUPS-3 Valve Heater Duty Cycle')
    pp.ylabel('Heater Duty Cycle by Month [%] \n (Total On-time / Total Time)')
    pp.savefig(msid+'_htr_dc.png')
    
    figure(5) 
    plot_cxctime(dates, on_freq, '*', mew=0)
    plot_cxctime(dates, on_freq)
    pp.title('MUPS-3 Valve Heater Cycling Frequency')
    pp.ylabel('Heater Cycles per Month')
    pp.savefig(msid+'_htr_cycle_freq.png')
    
    figure(6)
    plot_cxctime(dates, on_time/3600, '*', mew=0)
    plot_cxctime(dates, on_time/3600)
    pp.title('MUPS-3 Valve Heater On-Time')
    pp.ylabel('Heater On-Time by Month [hrs]')
    pp.savefig(msid+'_sum_htr_ontime.png')
    
    figure(7) 
    plot_cxctime(dates, avg_on_time/3600, '*', mew=0)
    plot_cxctime(dates, avg_on_time/3600)
    pp.title('MUPS-3 Valve Heater Average On-Time')
    pp.ylabel('Mean Heater On-Time by Month [hrs]')
    pp.savefig(msid+'_mean_htr_ontime.png')



















