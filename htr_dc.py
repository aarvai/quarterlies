from kadi import events
from utilities import append_to_array, find_first_after, same_limits, heat_map, count_by_month, sum_by_month, mean_by_month

close('all')

msid = 'PM3THV2T'
on_range = 60
off_range = 89 
t_start = '2000:001'
t_stop = None

temp = fetch.Msid(msid, t_start, t_stop)

def plot_htr_dc(temp, on_range, off_range):
 
    dt = diff(temp.vals)
    
    local_min = (append_to_array(dt <= 0., pos=0, val=bool(0)) & 
                 append_to_array(dt > 0., pos=-1, val=bool(0)))
    local_max = (append_to_array(dt >= 0., pos=0, val=bool(0)) & 
                 append_to_array(dt < 0., pos=-1, val=bool(0)))
    
    htr_on_range = temp.vals < on_range
    htr_off_range = temp.vals > off_range
    
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
    ylabel('On-Time Durations [sec]')
    title('MUPS-3 Valve Heater On-Time Durations')
    
    figure(2)
    plot_cxctime(temp.times, temp.vals, mew=0)
    plot_cxctime(temp.times, temp.vals, 'b*',mew=0)
    plot_cxctime(temp.times[htr_on], temp.vals[htr_on], 'c*',mew=0, label='Heater On')
    plot_cxctime(temp.times[htr_off], temp.vals[htr_off], 'r*',mew=0, label='Heater Off')
    legend()
    
    figure(3)
    hist(dur, bins=100, normed=True)
    xlabel('On-Time Durations [sec]')
    title('MUPS-3 Valve Heater On-Time Durations')
    
    figure(4)
    plot_cxctime(dates, dc*100, '*', mew=0)
    title('MUPS-3 Valve Heater Duty Cycle')
    ylabel('Heater Duty Cycle by Month [%] \n (Total On-time / Total Time)')
    
    figure(5)
    plot_cxctime(dates, on_freq, '*', mew=0)
    title('MUPS-3 Valve Heater Cycling Frequency')
    ylabel('Heater Cycles per Month')
    
    figure(6)
    plot_cxctime(dates, on_time/3600, '*', mew=0)
    title('MUPS-3 Valve Heater On-Time')
    ylabel('Heater On-Time by Month [hrs]')
    
    figure(7)
    plot_cxctime(dates, avg_on_time/3600, '*', mew=0)
    title('MUPS-3 Valve Heater Average On-Time')
    ylabel('Mean Heater On-Time by Month [hrs]')
    