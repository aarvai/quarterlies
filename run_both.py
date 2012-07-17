from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime
import numpy as np
from Chandra import Time
from matplotlib import pyplot as pp
from os import chdir, mkdir
import filter_times as bad

##-------------------------------------------------------------
# Inputs

t_start = '2012:032:00:00:00'
t_stop = '2012:150:00:00:00'

##-------------------------------------------------------------
# Run Quarterlies

pp.close('all')

t = Time.DateTime()
new_dir = t.date[:4] + '_' + t.date[5:8] + '_RUN'
mkdir(new_dir)

chdir(new_dir)
mkdir('pcad_' + t.date[:4] + '_' + t.date[5:8])
chdir('pcad_' + t.date[:4] + '_' + t.date[5:8])
#execfile('pcad_quarterly.py')
chdir('..')

mkdir('prop_' + t.date[:4] + '_' + t.date[5:8])
chdir('prop_' + t.date[:4] + '_' + t.date[5:8])
#execfile('prop_quarterly.py')
chdir('..')

##-------------------------------------------------------------
# LTTplot function

def LTTplot(var, **kwargs): 
    """Plot the daily min, max, and mean of a parameter from 2000:001 through 
    current
    
    :var:  MSID or derived parameter name (string)
    
    Optional inputs:
    :save:         Save to a .png with MSID's name (default is False)
    :limit_lines:  Plot database yellow caution and red warning limits 
                   (default is True)
    :yellow:       User-defined yellow caution limit lines (default is none)
    :red:          User-defined red warning limit lines  (default is none) 
    :ylim:         User-define  y-limits (default is none)
    :filter:       Start and End times to filter out due to bad data
    
    e.g.
    LTTplot('Dist_SatEarth')
    LTTplot('pline05t', ylim=[30,170], save=True) 
    LTTplot('pr1tv01t', limit_lines=False, yellow=150, red=240)
    LTTplot('pr2tv01t', limit_lines=False, yellow=[40,150], red=[37,240])
    LTTplot('plaed3gt', filter=['2011:299:00:00:00 2011:300:00:00:00'])
    """
    import filter_times as bad_times
    
    data = fetch.Msid(var,'2000:001',stat='daily')
    GRAY = '#999999'
    if kwargs.has_key('filter'):
        data.filter_bad_times(table=kwargs.pop('filter'))
    elseif hasattrib(bad_times, var):
        data.filter_bad_times(table=getattr(bad_times, var))
    pp.figure()
    plot_cxctime(data.times, data.mins, color=GRAY, label='daily min')
    plot_cxctime(data.times, data.maxes, 'k', label='daily max')
    plot_cxctime(data.times, data.means, 'g', label='daily mean')
    lim = kwargs.pop('limit_lines', True)
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
    else: pp.title(data.msid)
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
    s = kwargs.pop('save', True)
    if s == True:
        pp.savefig(data.msid.lower() + '.png')

