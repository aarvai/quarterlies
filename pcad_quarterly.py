from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime
from Chandra import Time
from matplotlib import pyplot as pp
import filter_times as bad_times
from os import chdir, mkdir, path

##-------------------------------------------------------------
# Define Custom LTT Plots

def pcad_LTTs(start, stop):

    # ACA --------------------------------------------
    #
    LTTplot('AACCCDPT', start=start, stop=stop, plot_limits=False, subplot=[2,1,1], savefig=False)
    LTTplot('AFLCAAH', start=start, stop=stop, plot_limits=False, cust_title='FLCA SOH - AFLCAAH', ylim=[4, 6.5], subplot=[2,1,2], samefig=True, saveas='01_ACA_TEMP_SOH.png')

    # Min CSS Counts in NPM, Sun ---------------------
    LTTplot('DP_CSS1_NPM_SUN', start=start, stop=stop, plot_limits=False, plot_means=False, plot_maxes=False, cust_title='MIN CSS-1 COUNTS IN NPM ONLY', cust_unit='COUNTS', subplot=[4,1,1], savefig=False)
    LTTplot('DP_CSS2_NPM_SUN', start=start, stop=stop, plot_limits=False, plot_means=False, plot_maxes=False, cust_title='MIN CSS-2 COUNTS IN NPM ONLY', cust_unit='COUNTS', subplot=[4,1,2], samefig=True, savefig=False)
    LTTplot('DP_CSS3_NPM_SUN', start=start, stop=stop, plot_limits=False, plot_means=False, plot_maxes=False, cust_title='MIN CSS-3 COUNTS IN NPM ONLY', cust_unit='COUNTS', subplot=[4,1,3], samefig=True, savefig=False)
    LTTplot('DP_CSS4_NPM_SUN', start=start, stop=stop, plot_limits=False, plot_means=False, plot_maxes=False, cust_title='MIN CSS-4 COUNTS IN NPM ONLY', cust_unit='COUNTS', subplot=[4,1,4], samefig=True, saveas='29_RW_TORQUE_CURR_2.png')      
    
    # FSS Angles -------------------------------------
    #
    LTTplot('DP_ROLL_FSS', cust_title='FSS ROLL ANGLE', cust_unit='DEG', start=start, stop=stop, plot_limits=False, subplot=[2,1,1], savefig=False)
    LTTplot('DP_PITCH_FSS', cust_title='FSS PITCH ANGLE', cust_unit='DEG', start=start, stop=stop, plot_limits=False, samefig=True, subplot=[2,1,2], saveas='18_FSS_ROLL_PITCH.png')
    #
    LTTplot('AOALPANG', start=start, stop=stop, plot_limits=False, subplot=[2,1,1], savefig=False)
    LTTplot('AOBETANG', start=start, stop=stop, plot_limits=False, subplot=[2,1,2], samefig=True, saveas='17_FSS_ALPHA_BETA.png')

    # FSS / CSS Sun Vector Difference ----------------
    LTTplot('DP_FSS_CSS_ANGLE_DIFF', start=start, stop=stop, plot_limits=False, saveas='30_FSS_CSS_ANGLE_DIFF.png')

    # Solar Array Angles -----------------------------
    #
    LTTplot('AOSARES1', start=start, stop=stop, plot_limits=False, subplot=[2,1,1], savefig=False)
    LTTplot('AOSARES2', start=start, stop=stop, plot_limits=False, subplot=[2,1,2], samefig=True, saveas='16_SA_RES_ANGLES.png')
    
    # IRU-1 ------------------------------------------
    if Time.DateTime(start) < Time.DateTime('2003:200'):
        if Time.DateTime(stop) > Time.DateTime('2003:200'):
            stop_iru1 = '2003:199'
        else:  
            stop_iru1 = stop
        #
        LTTplot('AIRU1G1I', start=start, stop=stop_iru1, plot_limits=False, subplot=[2,1,1], savefig=False)
        LTTplot('AIRU1G2I', start=start, stop=stop_iru1, plot_limits=False, subplot=[2,1,2], samefig=True, saveas='07_IRU_1_CURRENTS.png')
        #
        LTTplot('AIRU1G1T', start=start, stop=stop_iru1, plot_limits=False, plot_mins=False, plot_maxes=False, cust_title='MEAN IRU-1 GYRO #1 TEMP - AIRU1G1T', subplot=[2,1,1], savefig=False)
        LTTplot('AIRU1G2T', start=start, stop=stop_iru1, plot_limits=False, plot_mins=False, plot_maxes=False, cust_title='MEAN IRU-1 GYRO #2 TEMP - AIRU1G2T', subplot=[2,1,2], samefig=True, saveas='08_IRU_1_TEMPS_1.png')
        #
        LTTplot('AIRU1BT', start=start, stop=stop_iru1, plot_limits=False, plot_mins=False, plot_maxes=False, cust_title='MEAN IRU-1 BASE TEMPERATURE - AIRU1BT', subplot=[2,1,1], savefig=False)
        LTTplot('AIRU1VFT', start=start, stop=stop_iru1, plot_limits=False, plot_mins=False, plot_maxes=False, cust_title='MEAN IRU-1 VFC TEMPERATURE - AIRU1VFT', subplot=[2,1,2], samefig=True, saveas='09_IRU_1_TEMPS_2.png')

    # IRU-2 ------------------------------------------
    if Time.DateTime(stop) > Time.DateTime('2003:201'):
        if Time.DateTime(start) < Time.DateTime('2003:201'):
            start_iru1 = '2003:201'
        else:  
            start_iru1 = start
        #
        LTTplot('AIRU2G1I', start=start_iru1, stop=stop, plot_limits=False, subplot=[2,1,1], savefig=False)
        LTTplot('AIRU2G2I', start=start_iru1, stop=stop, plot_limits=False, subplot=[2,1,2], samefig=True, saveas='10_IRU_2_CURRENTS.png')
        #
        LTTplot('AIRU2G1T', start=start_iru1, stop=stop, plot_limits=False, plot_mins=False, plot_maxes=False, cust_title='MEAN IRU-2 GYRO #1 TEMP - AIRU2G1T', subplot=[2,1,1], savefig=False)
        LTTplot('AIRU2G2T', start=start_iru1, stop=stop, plot_limits=False, plot_mins=False, plot_maxes=False, cust_title='MEAN IRU-2 GYRO #2 TEMP - AIRU2G2T', subplot=[2,1,2], samefig=True, saveas='11_IRU_2_TEMPS_1.png')
        #
        LTTplot('AIRU2BT', start=start_iru1, stop=stop, plot_limits=False, plot_mins=False, plot_maxes=False, cust_title='MEAN IRU-2 BASE TEMPERATURE - AIRU2BT', subplot=[2,1,1], savefig=False)
        LTTplot('AIRU2VFT', start=start_iru1, stop=stop, plot_limits=False, plot_mins=False, plot_maxes=False, cust_title='MEAN IRU-2 VFC TEMPERATURE - AIRU2VFT', subplot=[2,1,2], samefig=True, saveas='12_IRU_2_TEMPS_2.png')

    # IRU Biases -------------------------------------
    #
    LTTplot('AOGBIAS1', start=start, stop=stop, plot_limits=False, cust_unit='ARCSEC/SEC', cust_mult=3600*180/pi, subplot=[3,1,1], savefig=False)
    LTTplot('AOGBIAS2', start=start, stop=stop, plot_limits=False, cust_unit='ARCSEC/SEC', cust_mult=3600*180/pi, subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('AOGBIAS3', start=start, stop=stop, plot_limits=False, cust_unit='ARCSEC/SEC', cust_mult=3600*180/pi, subplot=[3,1,3], samefig=True, saveas='28_IRU_GRYO_BIASES.png')

    # RW Speeds --------------------------------------
    #
    LTTplot('AORWSPD1', start=start, stop=stop, plot_limits=False, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,1], savefig=False)
    LTTplot('AORWSPD2', start=start, stop=stop, plot_limits=False, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('AORWSPD3', start=start, stop=stop, plot_limits=False, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,3], samefig=True, saveas='02_RW_SPEEDS_1.png')    
    #
    LTTplot('AORWSPD4', start=start, stop=stop, plot_limits=False, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,1], savefig=False)
    LTTplot('AORWSPD5', start=start, stop=stop, plot_limits=False, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('AORWSPD6', start=start, stop=stop, plot_limits=False, cust_unit='RPM', cust_mult=60/(pi*2), subplot=[3,1,3], samefig=True, saveas='3_RW_SPEEDS_2.png')    

    # RW Compartment Temperatures ------------------------
    LTTplot('TCYZ_RW1', start=start, stop=stop, plot_limits=False, subplot=[3,1,1], savefig=False)
    LTTplot('TPCP_RW2', start=start, stop=stop, plot_limits=False, subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('TPCP_RW3', start=start, stop=stop, plot_limits=False, subplot=[3,1,3], samefig=True, saveas='22_RW_COMP_TEMPS_1.png')    
    #
    LTTplot('TPCM_RW4', start=start, stop=stop, plot_limits=False, subplot=[3,1,1], savefig=False)
    LTTplot('TPCM_RW5', start=start, stop=stop, plot_limits=False, subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('TCYZ_RW6', start=start, stop=stop, plot_limits=False, subplot=[3,1,3], samefig=True, saveas='23_RW_COMP_TEMPS_2.png')      

    # RW Bearing Temperatures ------------------------
    LTTplot('ARWA1BT', start=start, stop=stop, plot_limits=False, subplot=[3,1,1], savefig=False)
    LTTplot('ARWA2BT', start=start, stop=stop, plot_limits=False, subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('ARWA3BT', start=start, stop=stop, plot_limits=False, subplot=[3,1,3], samefig=True, saveas='18_RW_BEARING_TEMPS_1.png')    
    #
    LTTplot('ARWA4BT', start=start, stop=stop, plot_limits=False, subplot=[3,1,1], savefig=False)
    LTTplot('ARWA5BT', start=start, stop=stop, plot_limits=False, subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('ARWA6BT', start=start, stop=stop, plot_limits=False, subplot=[3,1,3], samefig=True, saveas='19_RW_BEARING_TEMPS_2.png')      

    # RW Delta (Compartment - Bearing) Temperatures ------------------------
    LTTplot('DP_RW1_DELTA_TEMP', start=start, stop=stop, plot_limits=False, cust_title='RW-1 COMP - BEARING TEMP (TCYZ_RW1 - ARWA1BT)', cust_unit='DEG F', subplot=[3,1,1], savefig=False)
    LTTplot('DP_RW2_DELTA_TEMP', start=start, stop=stop, plot_limits=False, cust_title='RW-2 COMP - BEARING TEMP (TPCP_RW2 - ARWA1BT)', cust_unit='DEG F', subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('DP_RW3_DELTA_TEMP', start=start, stop=stop, plot_limits=False, cust_title='RW-3 COMP - BEARING TEMP (TPCP_RW3 - ARWA1BT)', cust_unit='DEG F', subplot=[3,1,3], samefig=True, saveas='24_RW_DELTA_TEMPS_1.png')    
    #
    LTTplot('DP_RW4_DELTA_TEMP', start=start, stop=stop, plot_limits=False, cust_title='RW-4 COMP - BEARING TEMP (TPCM_RW4 - ARWA1BT)', cust_unit='DEG F', subplot=[3,1,1], savefig=False)
    LTTplot('DP_RW5_DELTA_TEMP', start=start, stop=stop, plot_limits=False, cust_title='RW-5 COMP - BEARING TEMP (TPCM_RW5 - ARWA1BT)', cust_unit='DEG F', subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('DP_RW6_DELTA_TEMP', start=start, stop=stop, plot_limits=False, cust_title='RW-6 COMP - BEARING TEMP (TCYZ_RW6 - ARWA1BT)', cust_unit='DEG F', subplot=[3,1,3], samefig=True, saveas='25_RW_DELTA_TEMPS_2.png')      

    # RW Torque Currents -----------------------------
    #
    LTTplot('AWD1TQI', start=start, stop=stop, plot_limits=False, subplot=[3,1,1], savefig=False)
    LTTplot('AWD2TQI', start=start, stop=stop, plot_limits=False, subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('AWD3TQI', start=start, stop=stop, plot_limits=False, subplot=[3,1,3], samefig=True, saveas='20_RW_TORQUE_CURR_1.png')    
    #
    LTTplot('AWD4TQI', start=start, stop=stop, plot_limits=False, subplot=[3,1,1], savefig=False)
    LTTplot('AWD5TQI', start=start, stop=stop, plot_limits=False, subplot=[3,1,2], samefig=True, savefig=False)
    LTTplot('AWD6TQI', start=start, stop=stop, plot_limits=False, subplot=[3,1,3], samefig=True, saveas='21_RW_TORQUE_CURR_2.png')  

    # RW Drag Torque ---------------------------------
    #
    LTTplot('AORWCMD1', start=start, stop=stop, plot_limits=False, subplot=[3,1,1], plot_mins=False, plot_maxes=False, cust_title='MEAN RW #1 COMMANDED DRAG TORQUE - AORWCMD1', savefig=False)
    LTTplot('AORWCMD2', start=start, stop=stop, plot_limits=False, subplot=[3,1,2], plot_mins=False, plot_maxes=False, cust_title='MEAN RW #2 COMMANDED DRAG TORQUE - AORWCMD2', samefig=True, savefig=False)  
    LTTplot('AORWCMD3', start=start, stop=stop, plot_limits=False, subplot=[3,1,3], plot_mins=False, plot_maxes=False, cust_title='MEAN RW #3 COMMANDED DRAG TORQUE - AORWCMD3', samefig=True, saveas='14_RW_DRAG_TORQUE_1.png')   
    #
    LTTplot('AORWCMD4', start=start, stop=stop, plot_limits=False, subplot=[3,1,1], plot_mins=False, plot_maxes=False, cust_title='MEAN RW #4 COMMANDED DRAG TORQUE - AORWCMD4', savefig=False)
    LTTplot('AORWCMD5', start=start, stop=stop, plot_limits=False, subplot=[3,1,2], plot_mins=False, plot_maxes=False, cust_title='MEAN RW #5 COMMANDED DRAG TORQUE - AORWCMD5', samefig=True, savefig=False)  
    LTTplot('AORWCMD6', start=start, stop=stop, plot_limits=False, subplot=[3,1,3], plot_mins=False, plot_maxes=False, cust_title='MEAN RW #6 COMMANDED DRAG TORQUE - AORWCMD6', samefig=True, saveas='15_RW_DRAG_TORQUE_2.png')      
       
    # WDE Converter Voltages -------------------------
    #
    LTTplot('AWD1CV5V', start=start, stop=stop, plot_limits=False, subplot=[3,1,1], plot_mins=False, plot_maxes=False, cust_title='MEAN WDE-1 +5V CONVERTER VOLTAGE - AWD1CV5V', savefig=False)
    LTTplot('AWD2CV5V', start=start, stop=stop, plot_limits=False, subplot=[3,1,2], plot_mins=False, plot_maxes=False, cust_title='MEAN WDE-2 +5V CONVERTER VOLTAGE - AWD2CV5V', samefig=True, savefig=False)   
    LTTplot('AWD3CV5V', start=start, stop=stop, plot_limits=False, subplot=[3,1,3], plot_mins=False, plot_maxes=False, cust_title='MEAN WDE-3 +5V CONVERTER VOLTAGE - AWD3CV5V', samefig=True, saveas='26_CONV_VOLT_WDE_1.png') 
    #
    LTTplot('AWD4CV5V', start=start, stop=stop, plot_limits=False, subplot=[3,1,1], plot_mins=False, plot_maxes=False, cust_title='MEAN WDE-4 +5V CONVERTER VOLTAGE - AWD4CV5V', savefig=False)
    LTTplot('AWD5CV5V', start=start, stop=stop, plot_limits=False, subplot=[3,1,2], plot_mins=False, plot_maxes=False, cust_title='MEAN WDE-5 +5V CONVERTER VOLTAGE - AWD5CV5V', samefig=True, savefig=False)   
    LTTplot('AWD6CV5V', start=start, stop=stop, plot_limits=False, subplot=[3,1,3], plot_mins=False, plot_maxes=False, cust_title='MEAN WDE-6 +5V CONVERTER VOLTAGE - AWD6CV5V', samefig=True, saveas='27_CONV_VOLT_WDE_2.png') 

    # Other Converter Voltages -----------------------
    #
    LTTplot('ACPA5CV', start=start, stop=stop, plot_limits=False, subplot=[3,1,1], plot_mins=False, plot_maxes=False, cust_title='MEAN CPE-A +5V CONVERTER VOLTAGE - ACPA5CV', savefig=False)
    LTTplot('ADE1P5CV', start=start, stop=stop, plot_limits=False, subplot=[3,1,2], plot_mins=False, plot_maxes=False, cust_title='MEAN ADE-A +5V CONVERTER VOLTAGE - ADE1P5CV', samefig=True, savefig=False)   
    LTTplot('AFSSPC1V', start=start, stop=stop, plot_limits=False, subplot=[3,1,3], plot_mins=False, plot_maxes=False, cust_title='MEAN FSS-A +5V CONVERTER VOLTAGE - AFSSPC1V', samefig=True, saveas='04_CONV_VOLT_OTHER_1.png') 
    #
    LTTplot('AGWS1V', start=start, stop=stop, plot_limits=False, subplot=[3,1,1], plot_mins=False, plot_maxes=False, cust_title='MEAN GYRO WHEEL SUPPLY 1 INPUT VOLTAGE - AGWS1V', savefig=False)
    LTTplot('AGWS2V', start=start, stop=stop, plot_limits=False, subplot=[3,1,2], plot_mins=False, plot_maxes=False, cust_title='MEAN GYRO WHEEL SUPPLY 2 INPUT VOLTAGE - AGWS2V', samefig=True, savefig=False)
    LTTplot('AIOAP5CV', start=start, stop=stop, plot_limits=False, subplot=[3,1,3], plot_mins=False, plot_maxes=False, cust_title='MEAN IOE-A +5V CONVERTER VOLTAGE - AIOAP5CV', samefig=True, saveas='05_CONV_VOLT_OTHER_2.png')   
    #
    LTTplot('ASPEA5CV', start=start, stop=stop, plot_limits=False, subplot=[3,1,1], plot_mins=False, plot_maxes=False, cust_title='MEAN SPE-A +5V CONVERTER VOLTAGE - ASPEA5CV', savefig=False) 
    LTTplot('AVD1CV5V', start=start, stop=stop, plot_limits=False, subplot=[3,1,2], plot_mins=False, plot_maxes=False, cust_title='MEAN VDE-A +5V CONVERTER VOLTAGE - AVD1CV5V', samefig=True, saveas='06_CONV_VOLT_OTHER_3.png')    

    # EPIC Register Mismatches & CPE Error Count ------
    #
    LTTplot('AOEPICER', start=start, stop=stop, plot_limits=False, plot_stds=False, subplot=[2,1,1], savefig=False)
    LTTplot('AOCPESTC', start=start, stop=stop, plot_limits=False, subplot=[2,1,2], cust_title='CPE ERROR COUNT - AOCPESTC', samefig=True, saveas='13_EPIC_CPE.png') 

   
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