from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime
import numpy as np
from Chandra import Time
from matplotlib import pyplot as pp


pp.close('all')

#-------------------------------------------------------------
# MUPS Tank Pressure Update Plot

x=fetch.Msidset(['pmtank1t', 'pmtank2t', 'pmtank3t', 'pmfp01t', 'pmtankp',
                 'aosares1', 'aosares2'], '2009:100:00:00:00.000', 
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

vars=['plaev2bt','pm1thv1t','pm2thv1t','pm2thv2t','pr1tv01t']
col = ['b','g','r','c','m']
ys=np.array([[40,220],[90,180],[80,200],[90,180],[80,180]])
x = fetch.Msidset(vars,'2004:001',stat='daily')
for i in range(len(vars)):
    pp.subplot(5,1,i+1)
    plot_cxctime(x[vars[i]].times, x[vars[i]].maxes, col[i])
    pp.title(x[vars[i]].msid.upper() + ' Maximum Daily Temperature')
    pp.ylabel(x[vars[i]].unit)
    pp.ylim(ys[i])
pp.savefig('DropoutThermistorTemps.png')

##-------------------------------------------------------------
# Custom LTT Plots

LTTplot('pcm01t', ylim=[50,170], limit_lines=False, yellow=[85,145], 
        red=[80,160])
LTTplot('pcm02t', ylim=[50,170], limit_lines=False, yellow=[85,145], red=[80,160])
LTTplot('pcm03t', ylim=[50,170], limit_lines=False, yellow=[65,145], red=[60,160])
LTTplot('pcm04t', ylim=[50,170], limit_lines=False, yellow=[65,145], red=[60,160])
LTTplot('pfdm101t')
LTTplot('pfdm102t')
LTTplot('pfdm201t')
LTTplot('pfdm202t')
LTTplot('pffp01t', ylim=[30,250], limit_lines=False, yellow=[47,200],red=[40,240])
LTTplot('pftank1t', ylim=[30,130], limit_lines=False, yellow=[47,100], red=[40,120])
LTTplot('pftank2t', ylim=[30,130], limit_lines=False, yellow=[47,100], red=[40,120])
LTTplot('pftankip')
LTTplot('pftankop')
LTTplot('phetankp')
LTTplot('phetankt', ylim=[-20,150], limit_lines=False, yellow=[0,130], red=[-10,140])
LTTplot('phofp1t')
LTTplot('plaed1at', ylim=[-90,300])
LTTplot('plaed1bt', ylim=[-90,300])
LTTplot('plaed1ct', ylim=[-90,300])
LTTplot('plaed1dt', ylim=[-90,300])
LTTplot('plaed1et')
LTTplot('plaed1ft', ylim=[-90,300])
LTTplot('plaed1gt', ylim=[-90,300])
LTTplot('plaed1ht', ylim=[-90,300])
LTTplot('plaed1it')
LTTplot('plaed2at', 
        ylim=[-90,300])
LTTplot('plaed2bt', ylim=[-90,300])
LTTplot('plaed2ct')
LTTplot('plaed2dt')
LTTplot('plaed2et', ylim=[-90,300])
LTTplot('plaed2ft')
LTTplot('plaed2gt')
LTTplot('plaed2ht', ylim=[-90,300])
LTTplot('plaed2it', ylim=[-90,300])
LTTplot('plaed3at', ylim=[-90,100])
LTTplot('plaed3bt', ylim=[-90,100])
LTTplot('plaed3ct', ylim=[-90,100])
LTTplot('plaed3dt', ylim=[-90,100])
LTTplot('plaed3et')
LTTplot('plaed3ft')
LTTplot('plaed3gt', ylim=[-90,100])
LTTplot('plaed3ht')
LTTplot('plaed3it', ylim=[-90,100])
LTTplot('plaed4at', ylim=[-90,100])
LTTplot('plaed4bt', ylim=[-90,100])
LTTplot('plaed4ct')
LTTplot('plaed4dt', ylim=[-90,100])
LTTplot('plaed4et', ylim=[-90,100])
LTTplot('plaed4ft', ylim=[-90,100])
LTTplot('plaed4gt', ylim=[-90,100])
LTTplot('plaed4ht', ylim=[-90,100])
LTTplot('plaed4it', ylim=[-90,100])
LTTplot('plaev1at', ylim=[30,250], limit_lines=False, yellow=[47,225], 
        red=[40,240])
LTTplot('plaev1bt', ylim=[30,250], limit_lines=False, yellow=[47,225], 
        red=[40,240])
LTTplot('plaev2at', ylim=[30,250], limit_lines=False, yellow=[47,225], 
        red=[40,240])
LTTplot('plaev2bt', ylim=[30,250], limit_lines=False, yellow=[47,225], 
        red=[40,240])
LTTplot('plaev3at', ylim=[30,250], limit_lines=False, yellow=[47,225], 
        red=[40,240])
LTTplot('plaev3bt', ylim=[30,250], limit_lines=False, yellow=[47,225], 
        red=[40,240])
LTTplot('plaev4at', ylim=[30,250], limit_lines=False, yellow=[-200,225], 
        red=[-300,240])
LTTplot('plaev4bt', ylim=[30,250], limit_lines=False, yellow=[47,225], 
        red=[40,240])
LTTplot('pline01t')
LTTplot('pline02t', ylim=[30,190], limit_lines=False, yellow=[47,170], 
        red=[40,180])
LTTplot('pline03t', ylim=[29.5,190], limit_lines=False, yellow=[42.5,170], red=[39.5,180])
LTTplot('pline04t', ylim=[29.5,190], limit_lines=False, yellow=[42.5,170], red=[39.5,180])
LTTplot('pline05t', ylim=[30,250], limit_lines=False, yellow=[47,200], red=[40,240])
LTTplot('pline06t')
LTTplot('pline07t', ylim=[30,250], limit_lines=False, yellow=[47,200], red=[40,240])
LTTplot('pline08t')
LTTplot('pline09t')
LTTplot('pline10t')
LTTplot('pline11t')
LTTplot('pline12t')
LTTplot('pline13t')
LTTplot('pline14t')
LTTplot('pline15t')
LTTplot('pline16t')
LTTplot('pm1thv1t')
LTTplot('pm1thv2t')
LTTplot('pm2thv1t', ylim=[30,250], limit_lines=False, yellow=[47,195], red=[40,240])
LTTplot('pm2thv2t')
LTTplot('pm3thv1t')
LTTplot('pm3thv2t')
LTTplot('pm4thv1t')
LTTplot('pm4thv2t')
LTTplot('pmfp01t', ylim=[30,150], limit_lines=False, yellow=[47,130], red=[40,140])
LTTplot('pmtank1t')
LTTplot('pmtank2t')
LTTplot('pmtank3t')
LTTplot('pmtankp')
LTTplot('pr1tv01t')
LTTplot('pr1tv02t')
LTTplot('pr2tv01t')
LTTplot('pr2tv02t')
LTTplot('pr3tv01t')
LTTplot('pr3tv02t')
LTTplot('pr4tv01t')
LTTplot('pr4tv02t')
LTTplot('pxdm01t')
LTTplot('pxdm02t')
LTTplot('pxtank1t')
LTTplot('pxtank2t')
LTTplot('pxtankip')
LTTplot('pxtankop')

##-------------------------------------------------------------
# Custom Zoom LTT Plots

#mkdir zoom_plots
#cd zoom_plots
#LTTplot('pcm01t', ylim=[95,150], limit_lines=False, yellow=[85,145], 
#        red=[80,160])
#LTTplot('pcm02t', ylim=[95,150], limit_lines=False, yellow=[85,145], 
#        red=[80,160])
#LTTplot('pcm03t', ylim=[95,150], limit_lines=False, yellow=[65,145], 
#        red=[60,160])
#LTTplot('pcm04t', ylim=[95,150], limit_lines=False, yellow=[65,145], 
#        red=[60,160])
#LTTplot('pmtank1t', ylim=[65,105])
#LTTplot('pmtank2t', ylim=[65,105])
#LTTplot('pmtank3t', ylim=[65,105])
#LTTplot('pftank1t', ylim=[65,105], limit_lines=False, yellow=[47,100], 
#        red=[40,120])
#LTTplot('pftank2t', ylim=[65,105], limit_lines=False, yellow=[47,100], 
#        red=[40,120])
#LTTplot('pftankip', ylim=[275, 305])
#LTTplot('pftankop', ylim=[275, 305])
#LTTplot('pr1tv01t', ylim=[40, 160], 
#        filter=['2000:049:00:00:00 2000:050:00:00:00',
#                '2000:327:00:00:00 2000:328:00:00:00',
#                '2003:121:00:00:00 2003:122:00:00:00', 
#                '2004:200:00:00:00 2004:201:00:00:00'])
#LTTplot('pr1tv02t', ylim=[40, 160], 
#        filter=['2000:049:00:00:00 2000:050:00:00:00',
#                '2000:327:00:00:00 2000:328:00:00:00',
#                '2004:200:00:00:00 2004:201:00:00:00'])
#LTTplot('pr2tv01t', ylim=[40, 160], 
#        filter=['2000:049:00:00:00 2000:050:00:00:00',
#                '2000:327:00:00:00 2000:328:00:00:00',
#                '2004:200:00:00:00 2004:201:00:00:00'])
#LTTplot('pr2tv02t', ylim=[40, 160], 
#        filter=['2000:049:00:00:00 2000:050:00:00:00',
#                '2000:327:00:00:00 2000:328:00:00:00',
#                '2004:200:00:00:00 2004:201:00:00:00'])



















