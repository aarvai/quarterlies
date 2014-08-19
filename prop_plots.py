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
# IPS Tank Pressure vs Temperature

def ips_tank(stop):
    x=fetch.Msidset(['pftank2t', 'pftankip'], '2000:001', stop, stat='5min')
    x['pftank2t'].remove_intervals(events.safe_suns)
    x['pftankip'].remove_intervals(events.safe_suns)
    htr_on = [('2013:012', '2013:262')]
    x['pftank2t'].remove_intervals(htr_on)
    x['pftankip'].remove_intervals(htr_on)
    pp.figure()
    pp.plot(x['pftank2t'].midvals, x['pftankip'].midvals, 'b*-', mew=0, alpha=.1, label='historical range')
    now = DateTime().mjd
    past_yr = [(DateTime(now - 365, format='mjd').date, DateTime(now, format='mjd').date)]
    x['pftank2t'].select_intervals(past_yr)
    x['pftankip'].select_intervals(past_yr) 
    pp.plot(x['pftank2t'].midvals, x['pftankip'].midvals, 'r*-', mew=0, alpha=.1, label='past year')    
    pp.legend(loc='best')
    pp.xlim([65, 105])
    pp.ylim([275, 305])
    pp.grid()
    pp.title('IPS Tank Pressure vs Temperature \n (2000:001 onward excluding 2013 period w/ pri htr disabled)')
    pp.ylabel('PFTANKIP [psi]')
    pp.xlabel('PFTANK2T [deg F]')
    pp.tight_layout()
    pp.savefig('TankPressVsTemp.png')
    
#-------------------------------------------------------------
# Temperatures of Thermistors with Dropouts Plot

def therm_dropouts(stop):
    vars=['plaev2bt','pm1thv1t','pm1thv2t','pm2thv1t','pm2thv2t','pr1tv01t']
    col = ['b','g','r','c','m', '#CCCC00']
    ys=np.array([[40,220],[80,200],[80,200],[80,200],[80,200],[80,180]])
    x = fetch.Msidset(vars,'2004:001', stop, stat='daily')
    pp.figure(figsize=(8,12))
    for i in range(len(vars)):
        pp.subplot(len(vars),1,i+1)
        plot_cxctime(x[vars[i]].times, x[vars[i]].maxes, col[i])
        pp.title(x[vars[i]].msid.upper() + ' Maximum Daily Temperature')
        pp.ylabel(x[vars[i]].unit)
        pp.ylim(ys[i])
    pp.tight_layout()
    pp.savefig('DropoutThermistorTemps.png')

#-------------------------------------------------------------
# FDM-2 Temperatures

def fdm2(stop):
    vars=['pfdm201t', 'pfdm202t']
    x = fetch.Msidset(vars, '2009:001')
    pp.figure()
    pp.subplot(2,1,1)
    x['pfdm201t'].plot()
    pp.ylabel('Deg F')
    pp.title('PFDM201T:  FDM-2 Temp #1')
    pp.subplot(2,1,2)
    x['pfdm202t'].plot()
    pp.ylabel('Deg F')
    pp.title('PFDM202T:  FDM-2 Temp #2')    
    pp.savefig('FDM2.png')


















