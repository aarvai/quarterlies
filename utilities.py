import numpy as np
from os import chdir, mkdir, path
from matplotlib import pyplot as pp
from Chandra.Time import DateTime

from os import mkdir, chdir

def mkdir_cd(dir):
    # Make a directory (if doesn't already exist) and cd to it.
    if not path.exists(dir):
        mkdir(dir)
    chdir(dir) 

def smaller_axes(ax1):
    # Replace existing axes with one only 90% width and 75% height, 
    # allowing more room for ticks and titles
    ax_pos = ax1.get_position().get_points()
    ax_width = ax_pos[1,0] - ax_pos[0,0]
    ax_height = ax_pos[1,1] - ax_pos[0,1]
    pp.delaxes(ax1)
    ax2 = pp.axes([ax_pos[0,0] + .10 * ax_width, ax_pos[0,1] + .20 * ax_height, 
                  .90 * ax_width, .75 * ax_height])  
    return ax2

def reshape_array(array, num_rows, order='F'):
    # Return an array based on the values of the input array, but reshaped
    # with a user-specified number of rows.  Excess data will be trucated.
    #
    # Order = 'F' (column-major, FORTRAN-style)
    #       = 'C' (row-major, C-style)
    if np.mod(len(array),num_rows) > 0:
        out = array[:-np.mod(len(array), num_rows)].reshape((num_rows, np.floor(len(array) / int(num_rows))), order=order)
    else:
        out = array.reshape((num_rows, len(stdev) / int(num_rows)), order=order)
    return out

def count_by_month(times):
    """Counts the number of times an event occurs each month.
    Inputs a set of DateTime times (in any format). 
    Outputs an array of DateTime times spanning the timeframe with one entry per month
    and the count of events that occur within that month
    """    
    len_mo = 365.25/12*24*3600

    #Create an array that spans the timeframe with one date in the middle-ish of every month
    x_start = DateTime(min(DateTime(times).secs)).iso[:7] + '-15 12:00:00.00'
    x_stop = DateTime(max(DateTime(times).secs)).iso[:7] + '-15 12:00:00.00'
    x_times = np.arange(DateTime(x_start).secs, DateTime(x_stop).secs, len_mo) 
    
    #Collect the year and month for each date
    t_month = [DateTime(t).iso[:7] for t in times]
    x_month = [DateTime(x).iso[:7] for x in x_times]
    
    num_months = len(x_times)
    month_counts = np.zeros(num_months)
    for i in np.arange(num_months):
        match = [t == x_month[i] for t in t_month]
        month_counts[i] = np.sum(match)
    month_times = x_times
    return month_times, month_counts

def sum_by_month(times, vals):
    """Sums events by month.
    Inputs a set of DateTime times (in any format). 
    Outputs an array of DateTime times spanning the timeframe with one entry per month
    and the sum of events that occur within that month
    """    
    len_mo = 365.25/12*24*3600

    #Create an array that spans the timeframe with one date in the middle-ish of every month
    x_start = DateTime(min(DateTime(times).secs)).iso[:7] + '-15 12:00:00.00'
    x_stop = DateTime(max(DateTime(times).secs)).iso[:7] + '-15 12:00:00.00'
    x_times = np.arange(DateTime(x_start).secs, DateTime(x_stop).secs, len_mo) 
    
    #Collect the year and month for each date
    t_month = [DateTime(t).iso[:7] for t in times]
    x_month = [DateTime(x).iso[:7] for x in x_times]
    
    num_months = len(x_times)
    month_sums = np.zeros(num_months)
    for i in np.arange(num_months):
        match = np.array([t == x_month[i] for t in t_month])
        month_sums[i] = np.sum(vals[match])
    month_times = x_times
    return month_times, month_sums   

def mean_by_month(times, vals):
    """Sums events by month.
    Inputs a set of DateTime times (in any format). 
    Outputs an array of DateTime times spanning the timeframe with one entry per month
    and the sum of events that occur within that month
    """    
    len_mo = 365.25/12*24*3600

    #Create an array that spans the timeframe with one date in the middle-ish of every month
    x_start = DateTime(min(DateTime(times).secs)).iso[:7] + '-15 12:00:00.00'
    x_stop = DateTime(max(DateTime(times).secs)).iso[:7] + '-15 12:00:00.00'
    x_times = np.arange(DateTime(x_start).secs, DateTime(x_stop).secs, len_mo) 
    
    #Collect the year and month for each date
    t_month = [DateTime(t).iso[:7] for t in times]
    x_month = [DateTime(x).iso[:7] for x in x_times]
    
    num_months = len(x_times)
    month_means = np.zeros(num_months)
    for i in np.arange(num_months):
        match = np.array([t == x_month[i] for t in t_month])
        month_means[i] = np.mean(vals[match])
    month_times = x_times
    return month_times, month_means   
    
def heat_map(x, y, bins=(20,20), colorbar=True, **kwargs):
    """Plots a "heat map", i.e. a scatter plot highlighting density

    Based on an exmple from 
    http://www.physics.ucdavis.edu/~dwittman/Matplotlib-examples/

    Inputs: 
    x = x vals (as from a scatter plot)
    y = y vals (as from a scatter plot)
    bins = int or tuple bins to feed into histogram2d
    colorbar = whether or not to display colorbar (default=True)
    x_lim = x limits of plot
    y_lim = y_limits of plot
    """
    if kwargs.has_key('x_lim'):
        x_lim = kwargs.pop('x_lim')
    else:  
        x_lim = [np.min(x), np.max(x)]
    if kwargs.has_key('y_lim'):
        y_lim = kwargs.pop('y_lim')
    else:  
        y_lim = [min(y), max(y)]
    hist,xedges,yedges = np.histogram2d(x,y,bins=bins,range=[x_lim,y_lim])
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    pp.imshow(hist.T,extent=extent,interpolation='nearest',origin='lower', aspect='auto')
    if colorbar==True:
        pp.colorbar()
    pp.show()    

def same_limits(subs):
    """Sets the x-limits and y-limits for a given set of subplots
    equal to the collective mins and maxes
    
    Inputs:  
    subs = subplots (tuple of 3-digit subplot numbers)
    
    e.g.  same_limits((411, 412, 413, 414))
    """    
    all_limits = np.zeros((len(subs), 4))
    for sub, i in zip(subs, range(len(subs))):
        pp.subplot(sub)
        all_limits[i,:] = pp.axis()
    best_limits = (min(all_limits[:,0]), max(all_limits[:,1]), 
                   min(all_limits[:,2]), max(all_limits[:,3]))
    for i in subs:
        pp.subplot(i)
        pp.axis(best_limits)

def append_to_array(a, pos=-1, val=0):
    """Appends a zero (or user-defined value) to a given one-dimensional array, 
    either at the end (pos=-1) or beginning (pos=0).
    
    e.g. append_to_array(arange(5),pos=-1)
    returns array([0, 1, 2, 3, 4, 0])
    """
    val_a = np.array([val])
    if pos==0:
        out = np.concatenate([val_a, a])
    elif pos==-1:
        out = np.concatenate([a, val_a])
    return out    

def find_closest(a, b):
    """This function returns an array of length a with the indices of 
    array b that are closest to the values of array a.
    """
    a = np.atleast_1d(np.array(a))
    b = np.atleast_1d(np.array(b))
    out = [np.argmin(abs(b - a1)) for a1 in a]
    return out
    
def find_last_before(a, b):
    """This function returns an array of length a with the indices of 
    array b that are closest without going over the values of array a.
    (Bob Barker rules.  Assumes b is sorted by magnitude.)
    """
    out = np.searchsorted(b,a,side='left') - 1
    out[out==-1] = 0
    return out    
     
def find_first_after(a, b):
    """This function returns an array of length a with the indices of 
    array b that are closest without being less than the values of array a.
    (Opposite of Bob Barker rules.  Assumes b is sorted by magnitude.)
    """
    out = np.searchsorted(b,a,side='right')
    return out      