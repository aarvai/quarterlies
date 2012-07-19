from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime
import numpy as np
from Chandra import Time
from matplotlib import pyplot as pp
from os import chdir, mkdir, path
import filter_times as bad

##-------------------------------------------------------------
# Inputs

start = '2012:032:00:00:00'
stop = '2012:150:00:00:00'

##-------------------------------------------------------------
# LTTplot function

def LTTplot(var, **kwargs): 
    """Plot the daily min, max, and mean of a parameter, filtering for known
    bad data as listed in filter_times.py.
    
    :var:  MSID or derived parameter name (string)
    
    Optional inputs:
    :savefig:      Save and close figure (default is True)
    :saveas:       Name to save figure as (default is <MSID>.png)
    :start:        Start time (default is 2000:001)
    :stop:         Stop time (default is None)
    :stat:         Statistic type ('5min' or 'daily', default is 'daily')
    :limit_lines:  Plot database yellow caution and red warning limits 
                   (default is True)
    :yellow:       User-defined yellow caution limit lines (default is none)
    :red:          User-defined red warning limit lines  (default is none) 
    :ylim:         User-defined  y-limits (default is none)
    :filter:       User-defined Start and End times to filter out due to bad 
                   data.  If none are supplied, it will default to any listed 
                   in filter_times.py.  In addition, LTTplot will always filter
                   known NSM and SSM events as listed in filter_times.py (bad_all).
    :subplot:      Subplot information in list form.  If not supplied, a new
                   figure will be created.
    :cust_unit:    Custom unit to be displayed on y-axis label, typically for use 
                   with custom_mult or derived parameters (default is none)
    :custom_mult:  Custom multiplier, typically for use with custom unit 
                   (default is none)   
    :plot_mins:    Plot minimum values (default is True)
    :plot_means:   Plot mean values (default is True)
    :plot_maxes:   Plot maximum values (default is True)
    :legend:       Display legend (default is False)
    
    e.g.
    LTTplot('Dist_SatEarth')
    LTTplot('pline05t', ylim=[30,170], savefig=False) 
    LTTplot('pr1tv01t', limit_lines=False, yellow=150, red=240)
    LTTplot('pr2tv01t', limit_lines=False, yellow=[40,150], red=[37,240])
    LTTplot('plaed3gt', filter=['2011:299:00:00:00 2011:300:00:00:00'])
    LTTplot('pcm01t', subplot=[2,1,1], savefig=False) 
    LTTplot('dp_css1_npm_sun', plot_means=False, plot_maxes=False, legend=True)
    """
       
    var = var.lower()
    start = kwargs.pop('start', '2000:001')
    stop = kwargs.pop('stop', None)
    stat = kwargs.pop('stat', 'daily')
    data = fetch.Msid(var, start, stop, stat=stat)
    GRAY = '#999999'
    data.filter_bad_times(table=getattr(bad, 'bad_all'))
    if kwargs.has_key('filter'):
        data.filter_bad_times(table=kwargs.pop('filter'))
    elif hasattr(bad, 'bad_' + var):
        data.filter_bad_times(table=getattr(bad, 'bad_' + var))
    if kwargs.has_key('subplot'):
        sp = kwargs.get('subplot')
        pp.subplot(sp[0],sp[1],sp[2])
    else:  
        pp.figure()
    mult = kwargs.pop('cust_mult', 1)    
    lim = kwargs.pop('limit_lines', True)
    if mult!=1:
        lim=False
    if kwargs.pop('plot_maxes', True):
        plot_cxctime(data.times, data.maxes * mult, 'k', label=(stat + ' maxes'))
    if kwargs.pop('plot_means', True):
        plot_cxctime(data.times, data.means * mult, 'g', label=(stat + ' means'))
    if kwargs.pop('plot_mins', True):
        plot_cxctime(data.times, data.mins * mult, color=GRAY, label=(stat + ' min'))
    if hasattr(data, 'tdb'):
        pp.title(data.msid.upper() + ':  ' + data.tdb.technical_name)
        if lim == True:
            if size(data.tdb.Tlmt) == 1 and data.tdb.Tlmt is not None:
                pp.plot(pp.xlim(), np.array([data.tdb.Tlmt[4], 
                                             data.tdb.Tlmt[4]]), 'r')
                pp.plot(pp.xlim(), np.array([data.tdb.Tlmt[2], 
                                             data.tdb.Tlmt[2]]), 'y')
                pp.plot(pp.xlim(), np.array([data.tdb.Tlmt[3], 
                                             data.tdb.Tlmt[3]]), 'y')
                pp.plot(pp.xlim(), np.array([data.tdb.Tlmt[5], 
                                             data.tdb.Tlmt[5]]), 'r')  
                if ~kwargs.has_key('ylim'):
                    pp.ylim(np.array([data.tdb.Tlmt[4]-10.0, 
                                      data.tdb.Tlmt[5]+10.0]))
    else: pp.title(data.msid.upper())
    if kwargs.has_key('cust_unit'):
        pp.ylabel(kwargs.pop('cust_unit'))
    else:
        pp.ylabel(data.unit)
    pp.grid()
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
    if kwargs.pop('legend', False):
        legend(loc='best')
    tight_layout()
    s = kwargs.pop('savefig', True)
    if s == True:
        figname = kwargs.pop('saveas', data.msid.lower() + '.png')
        pp.savefig(figname)
        # pp.close()

##-------------------------------------------------------------
# Run Quarterlies

pp.close('all')

t = Time.DateTime()
new_dir = t.date[:4] + '_' + t.date[5:8] + '_RUN'
pcad_dir = 'pcad_' + t.date[:4] + '_' + t.date[5:8]
prop_dir = 'prop_' + t.date[:4] + '_' + t.date[5:8]

if not path.exists(new_dir):
    mkdir(new_dir)
chdir(new_dir)

if not path.exists(pcad_dir):
    mkdir(pcad_dir)
chdir(pcad_dir)
#execfile('/home/aarvai/python/quarterlies/pcad_quarterly.py')
chdir('..')

if not path.exists(prop_dir):
    mkdir(prop_dir)
chdir(prop_dir)
# execfile('/home/aarvai/python/quarterlies/prop_quarterly.py')
chdir('../..')
# pp.close('all')
