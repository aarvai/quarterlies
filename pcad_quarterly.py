from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime
from matplotlib import pyplot as pp
import filter_times as bad_times
from os import chdir, mkdir, path

##-------------------------------------------------------------
# Define Custom LTT Plots

def pcad_LTTs(start, stop):

    # IRU-1
    pp.figure()
    LTTplot('AIRU1G1I', start=start, stop=stop, subplot=[2,1,1], savefig=False)
    LTTplot('AIRU1G2I', start=start, stop=stop, subplot=[2,1,2], samefig=True, saveas='IRU_1_CURRENTS.png')
    pp.figure()
    LTTplot('AIRU1G1T', start=start, stop=stop, subplot=[2,1,1], savefig=False)
    LTTplot('AIRU1G2T', start=start, stop=stop, subplot=[2,1,2], samefig=True, saveas='IRU_1_TEMPS_1.png')
    pp.figure()
    LTTplot('AIRU1BT', start=start, stop=stop, subplot=[2,1,1], savefig=False)
    LTTplot('AIRU1VFT', start=start, stop=stop, subplot=[2,1,2], samefig=True, saveas='IRU_1_TEMPS_2.png')

    # IRU-2
    pp.figure()
    LTTplot('AIRU2G1I', start=start, stop=stop, subplot=[2,1,1], savefig=False)
    LTTplot('AIRU2G2I', start=start, stop=stop, subplot=[2,1,2], samefig=True, saveas='IRU_2_CURRENTS.png')
    pp.figure()
    LTTplot('AIRU2G1T', start=start, stop=stop, subplot=[2,1,1], savefig=False)
    LTTplot('AIRU2G2T', start=start, stop=stop, subplot=[2,1,2], samefig=True, saveas='IRU_2_TEMPS_1.png')
    pp.figure()
    LTTplot('AIRU2BT', start=start, stop=stop, subplot=[2,1,1], savefig=False)
    LTTplot('AIRU2VFT', start=start, stop=stop, subplot=[2,1,2], samefig=True, saveas='IRU_2_TEMPS_2.png')

    # Gyro Biases
    pp.figure()
    LTTplot('AOGBIAS1', start=start, stop=stop, cust_unit='ARCSEC/SEC', cust_mult=3600*180/pi, subplot=[3,1,1], savefig=False)
    LTTplot('AOGBIAS2', start=start, stop=stop, cust_unit='ARCSEC/SEC', cust_mult=3600*180/pi, subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('AOGBIAS3', start=start, stop=stop, cust_unit='ARCSEC/SEC', cust_mult=3600*180/pi, subplot=[3,1,3], samefig=True, saveas='IRU_GRYO_BIASES.png')

    # RW Speeds
    pp.figure()
    LTTplot('AORWSPD1', start=start, stop=stop, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,1], savefig=False)
    LTTplot('AORWSPD2', start=start, stop=stop, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('AORWSPD3', start=start, stop=stop, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,3], samefig=True, saveas='RW_SPEEDS_1.png')    

    pp.figure()
    LTTplot('AORWSPD4', start=start, stop=stop, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,1], savefig=False)
    LTTplot('AORWSPD5', start=start, stop=stop, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('AORWSPD6', start=start, stop=stop, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,3], samefig=True, saveas='RW_SPEEDS_2.png')    

    # RW Bearing Temperatures
    LTTplot('ARWA1BT', start=start, stop=stop, subplot=[3,1,1], savefig=False)
    LTTplot('ARWA2BT', start=start, stop=stop, subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('ARWA3BT', start=start, stop=stop, subplot=[3,1,3], samefig=True, saveas='RW_TEMPS_1.png')    

    pp.figure()
    LTTplot('ARWA4BT', start=start, stop=stop, subplot=[3,1,1], savefig=False)
    LTTplot('ARWA5BT', start=start, stop=stop, subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('ARWA6BT', start=start, stop=stop, subplot=[3,1,3], samefig=True, saveas='RW_TEMPS_2.png')      

    # RW Torque Currents
    pp.figure()
    LTTplot('AWD1TQI', start=start, stop=stop, subplot=[3,1,1], savefig=False)
    LTTplot('AWD2TQI', start=start, stop=stop, subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('AWD3TQI', start=start, stop=stop, subplot=[3,1,3], samefig=True, saveas='RW_TORQUE_CURR_1.png')    

    pp.figure()
    LTTplot('AWD4TQI', start=start, stop=stop, subplot=[3,1,1], savefig=False)
    LTTplot('AWD5TQI', start=start, stop=stop, subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('AWD6TQI', start=start, stop=stop, subplot=[3,1,3], samefig=True, saveas='RW_TORQUE_CURR_2.png')  

    # Min CSS Counts in NPM, Sun
    LTTplot('DP_CSS1_NPM_SUN', start=start, stop=stop, subplot=[4,1,1], plot_means=False, plot_maxes=False, savefig=False)
    LTTplot('DP_CSS2_NPM_SUN', start=start, stop=stop, subplot=[4,1,2], plot_means=False, plot_maxes=False, samefig=True, savefig=False)
    LTTplot('DP_CSS3_NPM_SUN', start=start, stop=stop, subplot=[4,1,3], plot_means=False, plot_maxes=False, samefig=True, savefig=False)
    LTTplot('DP_CSS4_NPM_SUN', start=start, stop=stop, subplot=[4,1,4], plot_means=False, plot_maxes=False, samefig=True, saveas='RW_TORQUE_CURR_2.png')      
    
    # FSS Angles
    pp.figure()
    LTTplot('DP_ROLL_FSS', cust_unit='DEG', start=start, stop=stop, subplot=[2,1,1], savefig=False)
    LTTplot('DP_PITCH_FSS', cust_unit='DEG', start=start, stop=stop, samefig=True, subplot=[2,1,2], saveas='FSS_ROLL_PITCH.png')

    pp.figure()
    LTTplot('AOALPANG', start=start, stop=stop, subplot=[2,1,1], savefig=False)
    LTTplot('AOBETANG', start=start, stop=stop, subplot=[2,1,2], samefig=True, saveas='FSS_ALPHA_BETA.png')

    # FSS / CSS Sun Vector Difference
    LTTplot('DP_FSS_CSS_ANGLE_DIFF', start=start, stop=stop, saveas='FSS_CSS_ANGLE_DIFF.png')

    # Solar Array Angles
    pp.figure()
    LTTplot('AOSARES1', start=start, stop=stop, subplot=[2,1,1], savefig=False)
    LTTplot('AOSARES2', start=start, stop=stop, subplot=[2,1,2], samefig=True, saveas='SA_RES_ANGLES.png')
    
    # ACA 
    pp.figure()
    LTTplot('AACCCDPT', start=start, stop=stop, subplot=[2,1,1], savefig=False)
    LTTplot('AFLCAAH', start=start, stop=stop, subplot=[2,1,2], samefig=True, saveas='ACA_TEMP_SOH.png')
    
    # WDE Converter Voltages
    pp.figure()
    LTTplot('AWD1CV5V', start=start, stop=stop, subplot=[3,1,1], savefig=False)
    LTTplot('AWD2CV5V', start=start, stop=stop, subplot=[3,1,2], samefig=True, savefig=False)   
    LTTplot('AWD3CV5V', start=start, stop=stop, subplot=[3,1,3], samefig=True, saveas='CONV_VOLT_WDE_1.png') 
    
    pp.figure()
    LTTplot('AWD4CV5V', start=start, stop=stop, subplot=[3,1,1], savefig=False)
    LTTplot('AWD5CV5V', start=start, stop=stop, subplot=[3,1,2], samefig=True, savefig=False)   
    LTTplot('AWD6CV5V', start=start, stop=stop, subplot=[3,1,3], samefig=True, saveas='CONV_VOLT_WDE_2.png') 

    # Other Converter Voltages
    pp.figure()
    LTTplot('ACPA5CV', start=start, stop=stop, subplot=[3,1,1], savefig=False)
    LTTplot('ADE1P5CV', start=start, stop=stop, subplot=[3,1,2], samefig=True, savefig=False)   
    LTTplot('AFSSPC1V', start=start, stop=stop, subplot=[3,1,3], samefig=True, saveas='CONV_VOLT_OTHER_1.png') 
    
    pp.figure()
    LTTplot('AGWS2V', start=start, stop=stop, subplot=[3,1,1], savefig=False)
    LTTplot('AIOAP5CV', start=start, stop=stop, subplot=[3,1,2], samefig=True, savefig=False)   
    LTTplot('ASPEA5CV', start=start, stop=stop, subplot=[3,1,3], samefig=True, saveas='CONV_VOLT_OTHER_2.png') 

    pp.figure()
    LTTplot('AVD1CV5V', start=start, stop=stop, subplot=[3,1,1], saveas='CONV_VOLT_OTHER_3.png')    

    # CPE
    pp.figure()
    LTTplot('AOEPICER', start=start, stop=stop, subplot=[2,1,1], savefig=False)
    LTTplot('AOCPESTC', start=start, stop=stop, subplot=[2,1,2], samefig=True, saveas='CPE.png') 

    # RW Drag Torque
    pp.figure()
    LTTplot('AORWCMD1', start=start, stop=stop, subplot=[3,1,1], savefig=False)
    LTTplot('AORWCMD2', start=start, stop=stop, subplot=[3,1,2], samefig=True, savefig=False)  
    LTTplot('AORWCMD3', start=start, stop=stop, subplot=[3,1,3], samefig=True, saveas='RW_DRAG_TORQUE_1.png')   
    
    pp.figure()
    LTTplot('AORWCMD4', start=start, stop=stop, subplot=[3,1,1], savefig=False)
    LTTplot('AORWCMD5', start=start, stop=stop, subplot=[3,1,2], samefig=True, savefig=False)  
    LTTplot('AORWCMD6', start=start, stop=stop, subplot=[3,1,3], samefig=True, saveas='RW_DRAG_TORQUE_2.png')      

##-------------------------------------------------------------
# Run LTT Plots

if not path.exists('mission'):
    mkdir('mission')
chdir('mission')
pcad_LTTs('2000:001', stop)
chdir('..')
if not path.exists('quarter'):
    mkdir('quarter')
chdir('quarter')
#pcad_LTTs(start, stop)
chdir('..')


##-------------------------------------------------------------
# TO ADD LATER:
##-------------------------------------------------------------
# Pointing Control and Stability
#temp=LTTquery([ltt_root 'A_PNT_CTRL_STAB.ltt'],time(1999275),tstop,'keep dat');
#LTTplot(temp,2)
# PITCH_CTRL, MEAN PITCH POINTING CONTROL, ARCSEC, MEAN
# YAW_CTRL, MEAN YAW POINTING CONTROL, ARCSEC, MEAN
# PITCH_STAB, PITCH_STAB, ARCSEC, MEAN
# YAW_STAB, YAW_STAB, ARCSEC, MEAN