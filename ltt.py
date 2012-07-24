import numpy as np
from matplotlib import pyplot as pp

from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime

import filter_times as bad

##-------------------------------------------------------------
# Long term trending plotting function

def plot_ltt(var, **kwargs): 
    """Plot the daily min, max, and mean of a parameter, filtering for known
    bad data as listed in filter_times.py.
    
    :var:  MSID or derived parameter name (string)
    
    Optional inputs:
    :savefig:      Save and close figure (default is True)
    :saveas:       Name to save figure as (default is <MSID>.png)
    :samefig:      Use current figure (default is False)
    :start:        Start time (default is 2000:001)
    :stop:         Stop time (default is None)
    :stat:         Statistic type ('5min' or 'daily', default is 'daily')
    :filter:       User-defined Start and End times to filter out due to bad 
                   data.  If none are supplied, it will default to any listed 
                   in filter_times.py.  In addition, LTTplot will always 
                   filter known NSM and SSM events as listed in 
                   filter_times.py (bad_all).
    :plot_stds:    Plot standard deviations (default is True)
    :plot_mins:    Plot minimum values (default is True)
    :plot_means:   Plot mean values (default is True)
    :plot_maxes:   Plot maximum values (default is True)
    :plot_limits:  Plot database yellow caution and red warning limits 
                   (default is True)
    :yellow:       User-defined yellow caution limit lines (default is none)
    :red:          User-defined red warning limit lines  (default is none)                
    :subplot:      Subplot information in [rows, columns, subplot number] 
                   (default is [1, 1, 1])
    :fig_width:    Figure width (default is 8).  Helpful if x-axis is crowded.
                   Irrelevant if samefig=True.
    :fig_height:   Figure height (default varies by number of subplots:  
                   6 for 1 row of subplots, 9 for 2 rows, otherwise 12).
                   Irrelevant if samefig=True.
    :ylim:         User-defined  y-limits (default is none)
    
    :legend:       Display legend (default is False)
    :cust_title:   Custom title (default is MSID and description)
    :cust_unit:    Custom unit to be displayed on y-axis label, typically for 
                   use with custom_mult or derived parameters (default is 
                   none)
    :custom_mult:  Custom multiplier, typically for use with custom unit 
                   (default is none)   
    
    e.g.
    LTTplot('Dist_SatEarth')
    LTTplot('pline05t', ylim=[30,170], savefig=False) 
    LTTplot('pr1tv01t', limit_lines=False, yellow=150, red=240)
    LTTplot('pr2tv01t', limit_lines=False, yellow=[40,150], red=[37,240])
    LTTplot('plaed3gt', filter=['2011:299:00:00:00 2011:300:00:00:00'])
    LTTplot('pcm01t', subplot=[4,1,1], savefig=False) 
    LTTplot('aogbias1', cust_unit='ARCSEC/SEC', cust_mult=3600*180/pi, 
            subplot=311)
    LTTplot('aosares1', start='2003:001', stop='2003:100', fig_width=10, 
            fig_height=6)
    LTTplot('dp_css1_npm_sun', plot_means=False, plot_maxes=False, 
             plot_stds=False, legend=True)
    """
    var = var.lower()
    start = kwargs.pop('start', '2000:001')
    stop = kwargs.pop('stop', None)
    stat = kwargs.pop('stat', 'daily')
    
    # Collect data and filter for bad points
    data = fetch.Msid(var, start, stop, stat=stat)
    data.filter_bad_times(table=getattr(bad, 'bad_ALL'))
    if kwargs.has_key('filter'):
        data.filter_bad_times(table=kwargs.pop('filter'))
    elif hasattr(bad, 'bad_' + var):
        data.filter_bad_times(table=getattr(bad, 'bad_' + var))
    
    # Define subplots and figure size
    # Figure size will vary depending on the number of subplots.
    # If plotting standard deviations, ax1 will only be used to reference default
    # axes size.  ax1 will be deleted and data will be plotted on ax2.
    sub = kwargs.pop('subplot', 111)
    # Convert subplot input to list form if provided by user as integer
    if isscalar(sub):
        sub = [int(str(sub)[0]), int(str(sub)[1]), int(str(sub)[2])]
    # Create a new figure unless using existing figure
    if not kwargs.pop('samefig', False):
        if kwargs.has_key('fig_height'):
            fig_height = kwargs.pop('fig_height')
        elif sub[0] == 1:  
            fig_height = 6
        elif sub[0] == 2:  
            fig_height = 6
        else:  
            fig_height = 12
        fig_width = kwargs.pop('fig_width', 8)
        pp.figure(figsize=(fig_width, fig_height))
    ax1 = pp.subplot(sub[0], sub[1], sub[2])
    if kwargs.get('plot_stds', True):
        ax_pos = ax1.get_position().get_points()
        ax_width = ax_pos[1,0] - ax_pos[0,0]
        ax_height = ax_pos[1,1] - ax_pos[0,1]
        pp.delaxes(ax1)
        ax2 = pp.axes([ax_pos[0,0], ax_pos[0,1] + .20 * ax_height, ax_width, .80 * ax_height])  
    
    # Plot data
    mult = kwargs.pop('cust_mult', 1)    
    lim = kwargs.pop('limit_lines', True)
    if kwargs.pop('plot_maxes', True):
        plot_cxctime(data.times, data.maxes * mult, 'g--', label=(stat + ' maxes'))
    if kwargs.pop('plot_mins', True):
        plot_cxctime(data.times, data.mins * mult, 'b:', label=(stat + ' mins'))
    if kwargs.pop('plot_means', True):
        plot_cxctime(data.times, data.means * mult, 'k+-', label=(stat + ' means'))
   
    # Plot limits
    if kwargs.pop('plot_limits', True):
        # Check if single limit set exists in TDB
        if hasattr(data, 'tdb') and size(data.tdb.Tlmt) == 1 and data.tdb.Tlmt is not None:
            pp.plot(pp.xlim(), np.array([data.tdb.Tlmt[4] * mult, 
                                         data.tdb.Tlmt[4] * mult]), 'r')
            pp.plot(pp.xlim(), np.array([data.tdb.Tlmt[2] * mult, 
                                         data.tdb.Tlmt[2] * mult]), 'y')
            pp.plot(pp.xlim(), np.array([data.tdb.Tlmt[3] * mult, 
                                         data.tdb.Tlmt[3] * mult]), 'y')
            pp.plot(pp.xlim(), np.array([data.tdb.Tlmt[5] * mult, 
                                         data.tdb.Tlmt[5] * mult]), 'r')  
            if ~kwargs.has_key('ylim'):
                pp.ylim(np.array([data.tdb.Tlmt[4]-10.0, 
                                  data.tdb.Tlmt[5]+10.0]))
    
    # Add title
    if kwargs.has_key('cust_title'):
        title = kwargs.pop('cust_title')
    elif hasattr(data, 'tdb'):
        title = data.tdb.technical_name + ' - ' + data.msid.upper() 
    else:
        title=data.msid.upper()    
    pp.title(title)
    
    # Account for custom y-labels
    if kwargs.has_key('cust_unit'):
        pp.ylabel(kwargs.pop('cust_unit'))
    else:
        pp.ylabel(data.unit)
    
    pp.grid()
    
    # Plot custom limit lines
    if kwargs.has_key('ylim'):
        pp.ylim(kwargs.pop('ylim'))
    if kwargs.has_key('yellow'):
        y = np.array([kwargs.pop('yellow')])
        for i in range(len(y)):
            pp.plot(pp.xlim(), np.array([y[i], y[i]]), 'y') 
    if kwargs.has_key('red'):
        r = np.array([kwargs.pop('red')])
        for i in range(len(r)):
            pp.plot(pp.xlim(), np.array([r[i], r[i]]), 'r')        
    
    # Add legend
    if kwargs.pop('legend', False):
        legend(loc='best')
    
    # Plot standard deviations on ax3
    if kwargs.get('plot_stds', True):
        ax2.set_xticklabels([])
        ax3 = pp.axes([ax_pos[0,0], ax_pos[0,1] + .05 * ax_height, ax_width, .15 * ax_height])
        ax3.set_yticklabels([])
        plot_cxctime(data.times, data.stds * mult, color='k', label=(stat + ' stdev'))
    
    # Save and close figure
    s = kwargs.pop('savefig', True)
    if s == True:
        figname = kwargs.pop('saveas', data.msid.lower() + '.png')
        pp.savefig(figname)
        # pp.close()
