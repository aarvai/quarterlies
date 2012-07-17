from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime
from matplotlib import pyplot as pp
import filter_times as bad_times

##-------------------------------------------------------------
# Run Plots
mkdir('mission')
chdir('mission')
pcad_plots(time(2000001), stop):
chdir('..')
mkdir('quarter')
chdir('quarter')
pcad_plots(start, stop):
chdir('..')

##-------------------------------------------------------------
# Define Plots

def pcad_plots(start, stop):

    # IRU-1
    pp.figure()
    LTTplot('AIRU1G1I', start=start, stop=stop, subplot=[2,1,1])
    LTTplot('AIRU1G2I', start=start, stop=stop, subplot=[2,1,2])
    pp.figure()
    LTTplot('AIRU1G1T', start=start, stop=stop, subplot=[2,1,1])
    LTTplot('AIRU1G2T', start=start, stop=stop, subplot=[2,1,2])
    pp.figure()
    LTTplot('AIRU1BT', start=start, stop=stop, subplot=[2,1,1])
    LTTplot('AIRU1VFT', start=start, stop=stop, subplot=[2,1,2])

    # IRU-2
    pp.figure()
    LTTplot('AIRU2G1I', start=start, stop=stop, subplot=[2,1,1])
    LTTplot('AIRU2G2I', start=start, stop=stop, subplot=[2,1,2])
    pp.figure()
    LTTplot('AIRU2G1T', start=start, stop=stop, subplot=[2,1,1])
    LTTplot('AIRU2G2T', start=start, stop=stop, subplot=[2,1,2])
    pp.figure()
    LTTplot('AIRU2BT', start=start, stop=stop, subplot=[2,1,1])
    LTTplot('AIRU2VFT', start=start, stop=stop, subplot=[2,1,2])

    # Gyro Biases
    pp.figure()
    LTTplot('AOGBIAS1', start=start, stop=stop, cust_unit='ARCSEC/SEC', cust_mult=3600*180/pi, subplot=[3,1,1])
    LTTplot('AOGBIAS2', start=start, stop=stop, cust_unit='ARCSEC/SEC', cust_mult=3600*180/pi, subplot=[3,1,2])
    LTTplot('AOGBIAS3', start=start, stop=stop, cust_unit='ARCSEC/SEC', cust_mult=3600*180/pi, subplot=[3,1,3])

    # RW Speeds
    pp.figure()
    LTTplot('AORWSPD1', start=start, stop=stop, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,1])
    LTTplot('AORWSPD2', start=start, stop=stop, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,2])
    LTTplot('AORWSPD3', start=start, stop=stop, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,3])    

    pp.figure()
    LTTplot('AORWSPD4', start=start, stop=stop, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,1])
    LTTplot('AORWSPD5', start=start, stop=stop, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,2])
    LTTplot('AORWSPD6', start=start, stop=stop, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,3])    

    # RW Bearing Temperatures
    LTTplot('ARWA1BT', start=start, stop=stop, subplot=[3,1,1])
    LTTplot('ARWA2BT', start=start, stop=stop, subplot=[3,1,2])
    LTTplot('ARWA3BT', start=start, stop=stop, subplot=[3,1,3])    

    pp.figure()
    LTTplot('ARWA4BT', start=start, stop=stop, subplot=[3,1,1])
    LTTplot('ARWA5BT', start=start, stop=stop, subplot=[3,1,2])
    LTTplot('ARWA6BT', start=start, stop=stop, subplot=[3,1,3])      

    # RW Torque Currents
    pp.figure()
    LTTplot('AWD1TQI', start=start, stop=stop, subplot=[3,1,1])
    LTTplot('AWD2TQI', start=start, stop=stop, subplot=[3,1,2])
    LTTplot('AWD3TQI', start=start, stop=stop, subplot=[3,1,3])    

    pp.figure()
    LTTplot('AWD4TQI', start=start, stop=stop, subplot=[3,1,1])
    LTTplot('AWD5TQI', start=start, stop=stop, subplot=[3,1,2])
    LTTplot('AWD6TQI', start=start, stop=stop, subplot=[3,1,3])  

    # Min CSS Counts in NPM, Sun
    msids = ['DP_CSS1_NPM_SUN', 'DP_CSS2_NPM_SUN', 'DP_CSS3_NPM_SUN', 'DP_CSS4_NPM_SUN']
    css = fetch.Msidset(msids, start, stop, stat='daily')
    pp.figure()
    for i in range(4):
        msid = msids[i]
        if hasattr(bad_times, msid):
            css[msid].filter_bad_times(table=getattr(bad_times, msid))
        subplot(4,1,1)
        plot_cxctime(css[msid].times, css[msid].mins, 'g')
        ylabel(css[msid].unit)
    
    # FSS Angles
    pp.figure()
    LTTplot('DP_ROLL_FSS', cust_unit='DEG', start=start, stop=stop, subplot=[2,1,1])
    LTTplot('DP_PITCH_FSS', cust_unit='DEG', start=start, stop=stop, subplot=[2,1,2])

    pp.figure()
    LTTplot('AOALPANG', start=start, stop=stop, subplot=[2,1,1])
    LTTplot('AOBETANG', start=start, stop=stop, subplot=[2,1,2])

    # FSS / CSS Sun Vector Difference
    LTTplot('DP_FSS_CSS_ANGLE_DIFF', start=start, stop=stop)

    # Solar Array Angles
    pp.figure()
    LTTplot('AOSARES1', start=start, stop=stop, subplot=[2,1,1])
    LTTplot('AOSARES2', start=start, stop=stop, subplot=[2,1,2])
    
    # ACA 
    pp.figure()
    LTTplot('AACCCDPT', start=start, stop=stop, subplot=[2,1,1])
    LTTplot('AFLCAAH', start=start, stop=stop, subplot=[2,1,2])
    
    # WDE Converter Voltages
    pp.figure()
    LTTplot('AWD1CV5V', start=start, stop=stop, subplot=[3,1,1])
    LTTplot('AWD2CV5V', start=start, stop=stop, subplot=[3,1,2])   
    LTTplot('AWD3CV5V', start=start, stop=stop, subplot=[3,1,3]) 
    
    pp.figure()
    LTTplot('AWD4CV5V', start=start, stop=stop, subplot=[3,1,1])
    LTTplot('AWD5CV5V', start=start, stop=stop, subplot=[3,1,2])   
    LTTplot('AWD6CV5V', start=start, stop=stop, subplot=[3,1,3]) 

    # Other Converter Voltages
    pp.figure()
    LTTplot('ACPA5CV', start=start, stop=stop, subplot=[3,1,1])
    LTTplot('ADE1P5CV', start=start, stop=stop, subplot=[3,1,2])   
    LTTplot('AFSSPC1V', start=start, stop=stop, subplot=[3,1,3]) 
    
    pp.figure()
    LTTplot('AGWS2V', start=start, stop=stop, subplot=[3,1,1])
    LTTplot('AIOAP5CV', start=start, stop=stop, subplot=[3,1,2])   
    LTTplot('ASPEA5CV', start=start, stop=stop, subplot=[3,1,3]) 

    pp.figure()
    LTTplot('AVD1CV5V', start=start, stop=stop, subplot=[3,1,1])    

    # CPE
    pp.figure()
    LTTplot('AOEPICER', start=start, stop=stop, subplot=[2,1,1])
    LTTplot('AOCPESTC', start=start, stop=stop, subplot=[2,1,2]) 

    # RW Drag Torque
    pp.figure()
    LTTplot('AORWCMD1', start=start, stop=stop, subplot=[3,1,1])
    LTTplot('AORWCMD2', start=start, stop=stop, subplot=[3,1,2])  
    LTTplot('AORWCMD3', start=start, stop=stop, subplot=[3,1,3])   
    
    pp.figure()
    LTTplot('AORWCMD4', start=start, stop=stop, subplot=[3,1,1])
    LTTplot('AORWCMD5', start=start, stop=stop, subplot=[3,1,2])  
    LTTplot('AORWCMD6', start=start, stop=stop, subplot=[3,1,3])      



# Pointing Control and Stability
#temp=LTTquery([ltt_root 'A_PNT_CTRL_STAB.ltt'],time(1999275),tstop,'keep dat');
#LTTplot(temp,2)
# PITCH_CTRL, MEAN PITCH POINTING CONTROL, ARCSEC, MEAN
# YAW_CTRL, MEAN YAW POINTING CONTROL, ARCSEC, MEAN
# PITCH_STAB, PITCH_STAB, ARCSEC, MEAN
# YAW_STAB, YAW_STAB, ARCSEC, MEAN