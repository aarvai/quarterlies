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
    plot_ltt('pcm01t', start=start, stop=stop, ylim=[50,170], plot_limits=False, yellow=[85,145], red=[80,160])
    plot_ltt('pcm02t', start=start, stop=stop, ylim=[50,170], plot_limits=False, yellow=[85,145], red=[80,160])
    plot_ltt('pcm03t', start=start, stop=stop, ylim=[50,170], plot_limits=False, yellow=[65,145], red=[60,160])
    plot_ltt('pcm04t', start=start, stop=stop, ylim=[50,170], plot_limits=False, yellow=[65,145], red=[60,160])
    plot_ltt('pfdm101t', start=start, stop=stop)
    plot_ltt('pfdm102t', start=start, stop=stop)
    plot_ltt('pfdm201t', start=start, stop=stop)
    plot_ltt('pfdm202t', start=start, stop=stop)
    plot_ltt('pffp01t', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,200],red=[40,240])
    plot_ltt('pftank1t', start=start, stop=stop, ylim=[30,130], plot_limits=False, yellow=[47,100], red=[40,120])
    plot_ltt('pftank2t', start=start, stop=stop, ylim=[30,130], plot_limits=False, yellow=[47,100], red=[40,120])
    plot_ltt('pftankip', start=start, stop=stop, plot_limits=False, yellow=[270, 296], red=[240, 300])
    plot_ltt('pftankop', start=start, stop=stop, plot_limits=False, yellow=[270, 296], red=[240, 300])
    plot_ltt('phetankp', start=start, stop=stop)
    plot_ltt('phetankt', start=start, stop=stop, ylim=[-20,150], plot_limits=False, yellow=[0,130], red=[-10,140])
    plot_ltt('phofp1t', start=start, stop=stop, plot_limits=False, yellow=[35, 110], red=[30, 120])
    plot_ltt('plaed1at', start=start, stop=stop, ylim=[-90,300])
    plot_ltt('plaed1bt', start=start, stop=stop, ylim=[-90,300])
    plot_ltt('plaed1ct', start=start, stop=stop, ylim=[-90,300])
    plot_ltt('plaed1dt', start=start, stop=stop, ylim=[-90,300])
    plot_ltt('plaed1et', start=start, stop=stop)
    plot_ltt('plaed1ft', start=start, stop=stop, ylim=[-90,300])
    plot_ltt('plaed1gt', start=start, stop=stop, ylim=[-90,300])
    plot_ltt('plaed1ht', start=start, stop=stop, ylim=[-90,300])
    plot_ltt('plaed1it', start=start, stop=stop)
    plot_ltt('plaed2at', start=start, stop=stop, ylim=[-90,300])
    plot_ltt('plaed2bt', start=start, stop=stop, ylim=[-90,300])
    plot_ltt('plaed2ct', start=start, stop=stop)
    plot_ltt('plaed2dt', start=start, stop=stop)
    plot_ltt('plaed2et', start=start, stop=stop, ylim=[-90,300])
    plot_ltt('plaed2ft', start=start, stop=stop)
    plot_ltt('plaed2gt', start=start, stop=stop)
    plot_ltt('plaed2ht', start=start, stop=stop, ylim=[-90,300])
    plot_ltt('plaed2it', start=start, stop=stop, ylim=[-90,300])
    plot_ltt('plaed3at', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaed3bt', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaed3ct', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaed3dt', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaed3et', start=start, stop=stop)
    plot_ltt('plaed3ft', start=start, stop=stop)
    plot_ltt('plaed3gt', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaed3ht', start=start, stop=stop)
    plot_ltt('plaed3it', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaed4at', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaed4bt', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaed4ct', start=start, stop=stop)
    plot_ltt('plaed4dt', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaed4et', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaed4ft', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaed4gt', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaed4ht', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaed4it', start=start, stop=stop, ylim=[-90,100])
    plot_ltt('plaev1at', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    plot_ltt('plaev1bt', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    plot_ltt('plaev2at', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    plot_ltt('plaev2bt', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    plot_ltt('plaev3at', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    plot_ltt('plaev3bt', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    plot_ltt('plaev4at', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[-200,225], red=[-300,240])
    plot_ltt('plaev4bt', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,225], red=[40,240])
    plot_ltt('pline01t', start=start, stop=stop)
    plot_ltt('pline02t', start=start, stop=stop, ylim=[30,190], plot_limits=False, yellow=[47,170], red=[40,180])
    plot_ltt('pline03t', start=start, stop=stop, ylim=[29.5,190], plot_limits=False, yellow=[42.5,170], red=[39.5,180])
    plot_ltt('pline04t', start=start, stop=stop, ylim=[29.5,190], plot_limits=False, yellow=[42.5,170], red=[39.5,180])
    plot_ltt('pline05t', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,200], red=[40,240])
    plot_ltt('pline06t', start=start, stop=stop)
    plot_ltt('pline07t', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,200], red=[40,240])
    plot_ltt('pline08t', start=start, stop=stop)
    plot_ltt('pline09t', start=start, stop=stop)
    plot_ltt('pline10t', start=start, stop=stop)
    plot_ltt('pline11t', start=start, stop=stop)
    plot_ltt('pline12t', start=start, stop=stop)
    plot_ltt('pline13t', start=start, stop=stop)
    plot_ltt('pline14t', start=start, stop=stop)
    plot_ltt('pline15t', start=start, stop=stop)
    plot_ltt('pline16t', start=start, stop=stop)
    plot_ltt('pm1thv1t', start=start, stop=stop)
    plot_ltt('pm1thv2t', start=start, stop=stop)
    plot_ltt('pm2thv1t', start=start, stop=stop, ylim=[30,250], plot_limits=False, yellow=[47,195], red=[40,240])
    plot_ltt('pm2thv2t', start=start, stop=stop)
    plot_ltt('pm3thv1t', start=start, stop=stop)
    plot_ltt('pm3thv2t', start=start, stop=stop)
    plot_ltt('pm4thv1t', start=start, stop=stop)
    plot_ltt('pm4thv2t', start=start, stop=stop)
    plot_ltt('pmfp01t', start=start, stop=stop, ylim=[30,150], plot_limits=False, yellow=[47,130], red=[40,140])
    plot_ltt('pmtank1t', start=start, stop=stop)
    plot_ltt('pmtank2t', start=start, stop=stop)
    plot_ltt('pmtank3t', start=start, stop=stop)
    plot_ltt('pmtankp', start=start, stop=stop)
    plot_ltt('pr1tv01t', start=start, stop=stop, plot_limits=False, yellow=[40, 195], red=[37, 240])
    plot_ltt('pr1tv02t', start=start, stop=stop, plot_limits=False, yellow=[40, 195], red=[37, 240])
    plot_ltt('pr2tv01t', start=start, stop=stop, plot_limits=False, yellow=[40, 195], red=[37, 240])
    plot_ltt('pr2tv02t', start=start, stop=stop, plot_limits=False, yellow=[40, 195], red=[37, 240])
    plot_ltt('pr3tv01t', start=start, stop=stop)
    plot_ltt('pr3tv02t', start=start, stop=stop)
    plot_ltt('pr4tv01t', start=start, stop=stop)
    plot_ltt('pr4tv02t', start=start, stop=stop)
    plot_ltt('pxdm01t', start=start, stop=stop)
    plot_ltt('pxdm02t', start=start, stop=stop)
    plot_ltt('pxtank1t', start=start, stop=stop)
    plot_ltt('pxtank2t', start=start, stop=stop)
    plot_ltt('pxtankip', start=start, stop=stop)
    plot_ltt('pxtankop', start=start, stop=stop)


##-------------------------------------------------------------
# Run Custom LTT Plots
prop_LTTs('2002:001:00:00:00', stop)
chdir('..')

##-------------------------------------------------------------
# Custom Zoom LTT Plots

#mkdir zoom_plots
#cd zoom_plots
#plot_ltt('pcm01t', ylim=[95,150], plot_limits=False, yellow=[85,145], 
#        red=[80,160])
#plot_ltt('pcm02t', ylim=[95,150], plot_limits=False, yellow=[85,145], 
#        red=[80,160])
#plot_ltt('pcm03t', ylim=[95,150], plot_limits=False, yellow=[65,145], 
#        red=[60,160])
#plot_ltt('pcm04t', ylim=[95,150], plot_limits=False, yellow=[65,145], 
#        red=[60,160])
#plot_ltt('pmtank1t', ylim=[65,105])
#plot_ltt('pmtank2t', ylim=[65,105])
#plot_ltt('pmtank3t', ylim=[65,105])
#plot_ltt('pftank1t', ylim=[65,105], plot_limits=False, yellow=[47,100], 
#        red=[40,120])
#plot_ltt('pftank2t', ylim=[65,105], plot_limits=False, yellow=[47,100], 
#        red=[40,120])
#plot_ltt('pftankip', ylim=[275, 305])
#plot_ltt('pftankop', ylim=[275, 305])
#plot_ltt('pr1tv01t', ylim=[40, 160], 
#        filter=['2000:049:00:00:00 2000:050:00:00:00',
#                '2000:327:00:00:00 2000:328:00:00:00',
#                '2003:121:00:00:00 2003:122:00:00:00', 
#                '2004:200:00:00:00 2004:201:00:00:00'])
#plot_ltt('pr1tv02t', ylim=[40, 160], 
#        filter=['2000:049:00:00:00 2000:050:00:00:00',
#                '2000:327:00:00:00 2000:328:00:00:00',
#                '2004:200:00:00:00 2004:201:00:00:00'])
#plot_ltt('pr2tv01t', ylim=[40, 160], 
#        filter=['2000:049:00:00:00 2000:050:00:00:00',
#                '2000:327:00:00:00 2000:328:00:00:00',
#                '2004:200:00:00:00 2004:201:00:00:00'])
#plot_ltt('pr2tv02t', ylim=[40, 160], 
#        filter=['2000:049:00:00:00 2000:050:00:00:00',
#                '2000:327:00:00:00 2000:328:00:00:00',
#                '2004:200:00:00:00 2004:201:00:00:00'])



















