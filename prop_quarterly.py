from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime
import numpy as np
from Chandra import Time
from matplotlib import pyplot as pp

pp.close('all')

if not path.exists('mission'):
    mkdir('mission')
chdir('mission')

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
# Define Custom LTT Plots
def prop_LTTs(start, stop):
    LTTplot('pcm01t', start=start, stop=stop, ylim=[50,170], plot_limits=False, yellow=[85,145], red=[80,160])
    LTTplot('pcm02t', start=start, stop=stop, ylim=[50,170], plot_limits=False, yellow=[85,145], red=[80,160])
    LTTplot('pcm03t', start=start, stop=stop, ylim=[50,170], plot_limits=False, yellow=[65,145], red=[60,160])
    LTTplot('pcm04t', start=start, stop=stop, ylim=[50,170], plot_limits=False, yellow=[65,145], red=[60,160])
    LTTplot('pfdm101t', start=start, stop=stop)
    LTTplot('pfdm102t', start=start, stop=stop)
    LTTplot('pfdm201t', start=start, stop=stop)
    LTTplot('pfdm202t', start=start, stop=stop)
    LTTplot('pffp01t', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,200],red=[40,240])
    LTTplot('pftank1t', start=start, stop=stop, ylim=[30,130], plot_limits=False, yellow=[47,100], red=[40,120])
    LTTplot('pftank2t', start=start, stop=stop, ylim=[30,130], plot_limits=False, yellow=[47,100], red=[40,120])
    LTTplot('pftankip', start=start, stop=stop, plot_limits=False, yellow=[270, 296], red=[240, 300])
    LTTplot('pftankop', start=start, stop=stop, plot_limits=False, yellow=[270, 296], red=[240, 300])
    LTTplot('phetankp', start=start, stop=stop)
    LTTplot('phetankt', start=start, stop=stop, ylim=[-20,150], plot_limits=False, yellow=[0,130], red=[-10,140])
    LTTplot('phofp1t', start=start, stop=stop, plot_limits=False, yellow=[35, 110], red=[30, 120])
    LTTplot('plaed1at', start=start, stop=stop, ylim=[-90,300])
    LTTplot('plaed1bt', start=start, stop=stop, ylim=[-90,300])
    LTTplot('plaed1ct', start=start, stop=stop, ylim=[-90,300])
    LTTplot('plaed1dt', start=start, stop=stop, ylim=[-90,300])
    LTTplot('plaed1et', start=start, stop=stop)
    LTTplot('plaed1ft', start=start, stop=stop, ylim=[-90,300])
    LTTplot('plaed1gt', start=start, stop=stop, ylim=[-90,300])
    LTTplot('plaed1ht', start=start, stop=stop, ylim=[-90,300])
    LTTplot('plaed1it', start=start, stop=stop)
    LTTplot('plaed2at', start=start, stop=stop, ylim=[-90,300])
    LTTplot('plaed2bt', start=start, stop=stop, ylim=[-90,300])
    LTTplot('plaed2ct', start=start, stop=stop)
    LTTplot('plaed2dt', start=start, stop=stop)
    LTTplot('plaed2et', start=start, stop=stop, ylim=[-90,300])
    LTTplot('plaed2ft', start=start, stop=stop)
    LTTplot('plaed2gt', start=start, stop=stop)
    LTTplot('plaed2ht', start=start, stop=stop, ylim=[-90,300])
    LTTplot('plaed2it', start=start, stop=stop, ylim=[-90,300])
    LTTplot('plaed3at', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaed3bt', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaed3ct', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaed3dt', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaed3et', start=start, stop=stop)
    LTTplot('plaed3ft', start=start, stop=stop)
    LTTplot('plaed3gt', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaed3ht', start=start, stop=stop)
    LTTplot('plaed3it', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaed4at', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaed4bt', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaed4ct', start=start, stop=stop)
    LTTplot('plaed4dt', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaed4et', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaed4ft', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaed4gt', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaed4ht', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaed4it', start=start, stop=stop, ylim=[-90,100])
    LTTplot('plaev1at', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    LTTplot('plaev1bt', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    LTTplot('plaev2at', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    LTTplot('plaev2bt', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    LTTplot('plaev3at', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    LTTplot('plaev3bt', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    LTTplot('plaev4at', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[-200,225], red=[-300,240])
    LTTplot('plaev4bt', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    LTTplot('pline01t', start=start, stop=stop)
    LTTplot('pline02t', start=start, stop=stop, ylim=[30,190], plot_limits=False, yellow=[47,170], red=[40,180])
    LTTplot('pline03t', start=start, stop=stop, ylim=[29.5,190], plot_limits=False, yellow=[42.5,170], red=[39.5,180])
    LTTplot('pline04t', start=start, stop=stop, ylim=[29.5,190], plot_limits=False, yellow=[42.5,170], red=[39.5,180])
    LTTplot('pline05t', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,200], red=[40,240])
    LTTplot('pline06t', start=start, stop=stop)
    LTTplot('pline07t', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,200], red=[40,240])
    LTTplot('pline08t', start=start, stop=stop)
    LTTplot('pline09t', start=start, stop=stop)
    LTTplot('pline10t', start=start, stop=stop)
    LTTplot('pline11t', start=start, stop=stop)
    LTTplot('pline12t', start=start, stop=stop)
    LTTplot('pline13t', start=start, stop=stop)
    LTTplot('pline14t', start=start, stop=stop)
    LTTplot('pline15t', start=start, stop=stop)
    LTTplot('pline16t', start=start, stop=stop)
    LTTplot('pm1thv1t', start=start, stop=stop)
    LTTplot('pm1thv2t', start=start, stop=stop)
    LTTplot('pm2thv1t', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,195], red=[40,240])
    LTTplot('pm2thv2t', start=start, stop=stop)
    LTTplot('pm3thv1t', start=start, stop=stop)
    LTTplot('pm3thv2t', start=start, stop=stop)
    LTTplot('pm4thv1t', start=start, stop=stop)
    LTTplot('pm4thv2t', start=start, stop=stop)
    LTTplot('pmfp01t', start=start, stop=stop, ylim=[30,150], plot_limits=False, yellow=[47,130], red=[40,140])
    LTTplot('pmtank1t', start=start, stop=stop)
    LTTplot('pmtank2t', start=start, stop=stop)
    LTTplot('pmtank3t', start=start, stop=stop)
    LTTplot('pmtankp', start=start, stop=stop)
    LTTplot('pr1tv01t', start=start, stop=stop, plot_limits=False, yellow=[40, 195], red=[37, 240])
    LTTplot('pr1tv02t', start=start, stop=stop, plot_limits=False, yellow=[40, 195], red=[37, 240])
    LTTplot('pr2tv01t', start=start, stop=stop, plot_limits=False, yellow=[40, 195], red=[37, 240])
    LTTplot('pr2tv02t', start=start, stop=stop, plot_limits=False, yellow=[40, 195], red=[37, 240])
    LTTplot('pr3tv01t', start=start, stop=stop)
    LTTplot('pr3tv02t', start=start, stop=stop)
    LTTplot('pr4tv01t', start=start, stop=stop)
    LTTplot('pr4tv02t', start=start, stop=stop)
    LTTplot('pxdm01t', start=start, stop=stop)
    LTTplot('pxdm02t', start=start, stop=stop)
    LTTplot('pxtank1t', start=start, stop=stop)
    LTTplot('pxtank2t', start=start, stop=stop)
    LTTplot('pxtankip', start=start, stop=stop)
    LTTplot('pxtankop', start=start, stop=stop)


##-------------------------------------------------------------
# Run Custom LTT Plots
prop_LTTs('2002:001:00:00:00', stop)
chdir('..')

##-------------------------------------------------------------
# Custom Zoom LTT Plots

#mkdir zoom_plots
#cd zoom_plots
#LTTplot('pcm01t', ylim=[95,150], plot_limits=False, yellow=[85,145], 
#        red=[80,160])
#LTTplot('pcm02t', ylim=[95,150], plot_limits=False, yellow=[85,145], 
#        red=[80,160])
#LTTplot('pcm03t', ylim=[95,150], plot_limits=False, yellow=[65,145], 
#        red=[60,160])
#LTTplot('pcm04t', ylim=[95,150], plot_limits=False, yellow=[65,145], 
#        red=[60,160])
#LTTplot('pmtank1t', ylim=[65,105])
#LTTplot('pmtank2t', ylim=[65,105])
#LTTplot('pmtank3t', ylim=[65,105])
#LTTplot('pftank1t', ylim=[65,105], plot_limits=False, yellow=[47,100], 
#        red=[40,120])
#LTTplot('pftank2t', ylim=[65,105], plot_limits=False, yellow=[47,100], 
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



















