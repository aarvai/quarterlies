import numpy as np
from matplotlib import pyplot as pp

from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime
from Chandra import Time

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
# Custom Zoom LTT Plots




















