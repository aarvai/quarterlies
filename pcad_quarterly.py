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
    LTTplot('AACCCDPT', **plot_AACCCDPT)
    LTTplot('AFLCAAH', **plot_AFLCAAH)

    # Min CSS Counts in NPM, Sun ---------------------
    LTTplot('DP_CSS1_NPM_SUN', **plot_DP_CSS1_NPM_SUN)
    LTTplot('DP_CSS2_NPM_SUN', **plot_DP_CSS2_NPM_SUN)
    LTTplot('DP_CSS3_NPM_SUN', **plot_DP_CSS3_NPM_SUN)
    LTTplot('DP_CSS4_NPM_SUN', **plot_DP_CSS4_NPM_SUN)  
    
    # FSS Angles -------------------------------------
    #
    LTTplot('DP_ROLL_FSS', **plot_DP_ROLL_FSS)          
    LTTplot('DP_PITCH_FSS', **plot_DP_PITCH_FSS)        
    #
    LTTplot('AOALPANG', **plot_AOALPANG)                
    LTTplot('AOBETANG', **plot_AOBETANG)                

    # FSS / CSS Sun Vector Difference ----------------
    LTTplot('DP_FSS_CSS_ANGLE_DIFF', **plot_DP_FSS_CSS_ANGLE_DIFF)            

    # Solar Array Angles -----------------------------
    #
    LTTplot('AOSARES1', **plot_AOSARES1)               
    LTTplot('AOSARES2', **plot_AOSARES2)               
    
    # IRU-1 ------------------------------------------
    if Time.DateTime(start) < Time.DateTime('2003:200'):
        if Time.DateTime(stop) > Time.DateTime('2003:200'):
            stop_iru1 = '2003:199'
        else:  
            stop_iru1 = stop
        #
        LTTplot('AIRU1G1I', **plot_AIRU1G1I)              
        LTTplot('AIRU1G2I', **plot_AIRU1G2I)              
        #
        LTTplot('AIRU1G1T', **plot_AIRU1G1T)              
        LTTplot('AIRU1G2T', **plot_AIRU1G2T)              
        #
        LTTplot('AIRU1BT', **plot_AIRU1BT)                
        LTTplot('AIRU1VFT', **plot_AIRU1VFT)              

    # IRU-2 ------------------------------------------
    if Time.DateTime(stop) > Time.DateTime('2003:201'):
        if Time.DateTime(start) < Time.DateTime('2003:201'):
            start_iru1 = '2003:201'
        else:  
            start_iru1 = start
        #
        LTTplot('AIRU2G1I', **plot_AIRU2G1I)              
        LTTplot('AIRU2G2I', **plot_AIRU2G2I)              
        #
        LTTplot('AIRU2G1T', **plot_AIRU2G1T)              
        LTTplot('AIRU2G2T', **plot_AIRU2G2T)              
        #
        LTTplot('AIRU2BT', **plot_AIRU2BT)                
        LTTplot('AIRU2VFT', **plot_AIRU2VFT)              

    # IRU Biases -------------------------------------
    #
    LTTplot('AOGBIAS1', **plot_AOGBIAS1)                
    LTTplot('AOGBIAS2', **plot_AOGBIAS2)                
    LTTplot('AOGBIAS3', **plot_AOGBIAS3)                

    # RW Speeds --------------------------------------
    #
    LTTplot('AORWSPD1', **plot_AORWSPD1)                
    LTTplot('AORWSPD2', **plot_AORWSPD2)                
    LTTplot('AORWSPD3', **plot_AORWSPD3)                
    #
    LTTplot('AORWSPD4', **plot_AORWSPD4)                
    LTTplot('AORWSPD5', **plot_AORWSPD5)                
    LTTplot('AORWSPD6', **plot_AORWSPD6)                

    # RW Compartment Temperatures ------------------------
    LTTplot('TCYZ_RW1', **plot_TCYZ_RW1)                
    LTTplot('TPCP_RW2', **plot_TPCP_RW2)                
    LTTplot('TPCP_RW3', **plot_TPCP_RW3)                
    #
    LTTplot('TPCM_RW4', **plot_TPCM_RW4)                
    LTTplot('TPCM_RW5', **plot_TPCM_RW5)                
    LTTplot('TCYZ_RW6', **plot_TCYZ_RW6)                

    # RW Bearing Temperatures ------------------------
    LTTplot('ARWA1BT', **plot_ARWA1BT)                 
    LTTplot('ARWA2BT', **plot_ARWA2BT)                 
    LTTplot('ARWA3BT', **plot_ARWA3BT)                 
    #
    LTTplot('ARWA4BT', **plot_ARWA4BT)                 
    LTTplot('ARWA5BT', **plot_ARWA5BT)                 
    LTTplot('ARWA6BT', **plot_ARWA6BT)                 

    # RW Delta (Compartment - Bearing) Temperatures ------
    LTTplot('DP_RW1_DELTA_TEMP', **plot_DP_RW1_DELTA_TEMP)
    LTTplot('DP_RW2_DELTA_TEMP', **plot_DP_RW2_DELTA_TEMP)
    LTTplot('DP_RW3_DELTA_TEMP', **plot_DP_RW3_DELTA_TEMP)
    #
    LTTplot('DP_RW4_DELTA_TEMP', **plot_DP_RW4_DELTA_TEMP)
    LTTplot('DP_RW5_DELTA_TEMP', **plot_DP_RW5_DELTA_TEMP)
    LTTplot('DP_RW6_DELTA_TEMP', **plot_DP_RW6_DELTA_TEMP)

    # RW Torque Currents -----------------------------
    #
    LTTplot('AWD1TQI', **plot_AWD1TQI)                 
    LTTplot('AWD2TQI', **plot_AWD2TQI)                 
    LTTplot('AWD3TQI', **plot_AWD3TQI)                 
    #
    LTTplot('AWD4TQI', **plot_AWD4TQI)                 
    LTTplot('AWD5TQI', **plot_AWD5TQI)                 
    LTTplot('AWD6TQI', **plot_AWD6TQI)                 

    # RW Drag Torque ---------------------------------
    #
    LTTplot('AORWCMD1', **plot_AORWCMD1)               
    LTTplot('AORWCMD2', **plot_AORWCMD2)               
    LTTplot('AORWCMD3', **plot_AORWCMD3)               
    #
    LTTplot('AORWCMD4', **plot_AORWCMD4)               
    LTTplot('AORWCMD5', **plot_AORWCMD5)               
    LTTplot('AORWCMD6', **plot_AORWCMD6)               
       
    # WDE Converter Voltages -------------------------
    #
    LTTplot('AWD1CV5V', **plot_AWD1CV5V)               
    LTTplot('AWD2CV5V', **plot_AWD2CV5V)               
    LTTplot('AWD3CV5V', **plot_AWD3CV5V)               
    #
    LTTplot('AWD4CV5V', **plot_AWD4CV5V)               
    LTTplot('AWD5CV5V', **plot_AWD5CV5V)               
    LTTplot('AWD6CV5V', **plot_AWD6CV5V)               

    # Other Converter Voltages -----------------------
    #
    LTTplot('ACPA5CV', **plot_ACPA5CV)           
    LTTplot('ADE1P5CV', **plot_ADE1P5CV)         
    LTTplot('AFSSPC1V', **plot_AFSSPC1V)         
    #
    LTTplot('AGWS1V', **plot_AGWS1V)             
    LTTplot('AGWS2V', **plot_AGWS2V)             
    LTTplot('AIOAP5CV', **plot_AIOAP5CV)         
    #
    LTTplot('ASPEA5CV', **plot_ASPEA5CV)               
    LTTplot('AVD1CV5V', **plot_AVD1CV5V)               

    # EPIC Register Mismatches & CPE Error Count ------
    #
    LTTplot('AOEPICER', **plot_AOEPICER)               
    LTTplot('AOCPESTC', **plot_AOCPESTC)               

   
##-----------------------------------------------------
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