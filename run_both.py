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
# Run Quarterlies

pp.close('all')

t = Time.DateTime()
new_dir = t.date[:4] + '_' + t.date[5:8] + '_RUN'
pcad_dir = 'pcad_' + t.date[:4] + '_' + t.date[5:8]
prop_dir = 'prop_' + t.date[:4] + '_' + t.date[5:8]

if ~path.exists(new_dir):
    mkdir(new_dir)

chdir(new_dir)
if ~path.exists(pcad_dir):
    mkdir(pcad_dir)
chdir(pcad_dir)
execfile('pcad_quarterly.py')
chdir('..')

if ~path.exists(prop_dir):
    mkdir(prop_dir)
    chdir(prop_dir)
execfile('prop_quarterly.py')
chdir('..')

##-------------------------------------------------------------
# LTTplot function

def LTTplot(var, **kwargs): 
    """Plot the daily min, max, and mean of a parameter from 2000:001 through 
    current
    
    :var:  MSID or derived parameter name (string)
    
    Optional inputs:
    :savefig:      Save to a .png with MSID's name (default is True)
    :start:        Start time (default is 2000:001)
    :stop:         Stop time (default is None)
    :stat:         Statistic type ('5min' or 'daily', default is 'daily')
    :limit_lines:  Plot database yellow caution and red warning limits 
                   (default is True)
    :yellow:       User-defined yellow caution limit lines (default is none)
    :red:          User-defined red warning limit lines  (default is none) 
    :ylim:         User-define  y-limits (default is none)
    :filter:       Start and End times to filter out due to bad data.  If
                   none are supplied, it will default to any listed in
                   filter_times.py.
    :subplot:      Subplot information in list form.  If not supplied, a new
                   figure will be created.
    :cust_unit:    Custom unit, typically for use with custom_mult (default 
                   is none)
    :custom_mult:  Custom multiplier, typically for use with custom unit 
                   (default is none)
    e.g.
    LTTplot('Dist_SatEarth')
    LTTplot('pline05t', ylim=[30,170], savefig=False) 
    LTTplot('pr1tv01t', limit_lines=False, yellow=150, red=240)
    LTTplot('pr2tv01t', limit_lines=False, yellow=[40,150], red=[37,240])
    LTTplot('plaed3gt', filter=['2011:299:00:00:00 2011:300:00:00:00'])
    LTTplot('pcm01t', subplot=[2,1,1], savefig=False) 
    """
    import filter_times as bad_times
    
    var = var.lower()
    start = kwargs.pop('start', '2000:001')
    stop = kwargs.pop('stop', None)
    stat = kwargs.pop('stat', 'daily')
    data = fetch.Msid(var, start, stop, stat=stat)
    GRAY = '#999999'
    if kwargs.has_key('filter'):
        data.filter_bad_times(table=kwargs.pop('filter'))
    elif hasattr(bad_times, var):
        data.filter_bad_times(table=getattr(bad_times, 'bad_' + var))
    if kwargs.has_key('subplot'):
        sp = kwargs.pop('subplot')
        pp.subplot(sp[0],sp[1],sp[2])
    else:  
        pp.figure()
    mult = kwargs.pop('cust_mult', 1)    
    lim = kwargs.pop('limit_lines', True)
    if mult!=1:
        lim=False
    plot_cxctime(data.times, data.mins * mult, color=GRAY, label='min')
    plot_cxctime(data.times, data.maxes * mult, 'k', label='max')
    plot_cxctime(data.times, data.means * mult, 'g', label='mean')
    if hasattr(data, 'tdb'):
        pp.title(data.msid.upper() + ':  ' + data.tdb.technical_name)
        if lim == True:
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
    s = kwargs.pop('savefig', True)
    if s == True:
        pp.savefig(data.msid.lower() + '.png')
        pp.close()

