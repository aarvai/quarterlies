from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime
import numpy as np
from Chandra import Time
from matplotlib import pyplot as pp

##-------------------------------------------------------------
# Run Plots
mkdir('mission')
chdir('mission')
pcad_plots(time(2000001), tstop):
chdir('..')
mkdir('quarter')
chdir('quarter')
pcad_plots(tstart, tstop):
chdir('..')

##-------------------------------------------------------------
# Define Plots

def pcad_plots(tstart, tstop):
    subplot(2,1,1)
    LTTplot('AIRU1G1I')
    subplot(2,1,2)
    LTTplot('AIRU1G2I')
    figure()
    subplot(2,1,1)
    LTTplot('AIRU1G1T')
    LTTplot('AIRU1G2T')
    LTTplot('AIRU1BT')
    LTTplot('AIRU1VFT')
    
    
LTTplot('pftank1t', filter=['2000:049:00:00:00 2000:050:00:00:00'], 
        ylim=[30,130], limit_lines=False, yellow=[47,100], red=[40,120], 
        save=True)    
    
temp=LTTquery([ltt_root 'A_IRU-1.ltt'],time(1999250),time(2003200),'keep dat');
LTTplot(temp,2)
AIRU1G1I
AIRU1G2I
AIRU1G1T
AIRU1G2T
AIRU1BT,
AIRU1VFT

temp=LTTquery([ltt_root 'A_IRU-2.ltt'],time(2003201),tstop,'keep dat');
LTTplot(temp,2)
AIRU2G1I 
AIRU2G2I 
AIRU2G1T 
AIRU2G2T 
AIRU2BT 
AIRU2VFT

temp=LTTquery([ltt_root 'A_GYRO_BIAS.ltt'],time(1999275),tstop,'keep dat');
LTTplot(temp,3)
GCA_BIAS1 
GCA_BIAS2
GCA_BIAS3 
ROLL_BIAS_DIFF
PITCH_BIAS_DIFF
YAW_BIAS_DIFF
AOGBIAS1 
AOGBIAS2 
AOGBIAS3

temp=LTTquery([ltt_root 'A_RW_SPEED.ltt'],time(1999250),tstop,'keep dat');
LTTplot(temp,3)




temp=LTTquery([ltt_root 'A_RW_CURRENT_TEMP.ltt'],time(1999230),tstop,'keep dat');
LTTplot(temp,3)



temp=LTTquery([ltt_root 'A_FSS_CSS.ltt'],time(1999275),tstop,'keep dat');
LTTplot(temp,4)



temp=LTTquery([ltt_root 'A_FSS_CSS_2.ltt'],time(1999275),tstop,'keep dat');
LTTplot(temp,1)



temp=LTTquery([ltt_root 'A_ATTITUDE.ltt'],time(1999230),tstop,'keep dat');
LTTplot(temp,2)



temp=LTTquery([ltt_root 'A_PNT_CTRL_STAB.ltt'],time(1999275),tstop,'keep dat');
LTTplot(temp,2)



temp=LTTquery([ltt_root 'A_PEA_FLCA.ltt'],time(1999230),tstop,'keep dat');
LTTplot(temp,3)



temp=LTTquery([ltt_root 'A_WDE_CONV_VOLTAGE.ltt'],time(1999230),tstop,'keep dat');
LTTplot(temp,3)



temp=LTTquery([ltt_root 'A_A_CONV_VOLTAGE.ltt'],time(1999230),tstop,'keep dat');
LTTplot(temp,3)



temp=LTTquery([ltt_root 'A_HW_ERR.ltt'],time(1999230),tstop,'keep dat');
LTTplot(temp,2)



temp=LTTquery([ltt_root 'A_RW_DRAG_TORQUE.ltt'],time(1999250),tstop,'keep dat');
LTTplot(temp,3)




