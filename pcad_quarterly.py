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
    plot_ltt('AACCCDPT', **plot_AACCCDPT)
    plot_ltt('AFLCAAH', **plot_AFLCAAH)

    # Min CSS Counts in NPM, Sun ---------------------
    plot_ltt('DP_CSS1_NPM_SUN', **plot_DP_CSS1_NPM_SUN)
    plot_ltt('DP_CSS2_NPM_SUN', **plot_DP_CSS2_NPM_SUN)
    plot_ltt('DP_CSS3_NPM_SUN', **plot_DP_CSS3_NPM_SUN)
    plot_ltt('DP_CSS4_NPM_SUN', **plot_DP_CSS4_NPM_SUN)  
    
    # FSS Angles -------------------------------------
    #
    plot_ltt('DP_ROLL_FSS', **plot_DP_ROLL_FSS)          
    plot_ltt('DP_PITCH_FSS', **plot_DP_PITCH_FSS)        
    #
    plot_ltt('AOALPANG', **plot_AOALPANG)                
    plot_ltt('AOBETANG', **plot_AOBETANG)                

    # FSS / CSS Sun Vector Difference ----------------
    plot_ltt('DP_FSS_CSS_ANGLE_DIFF', **plot_DP_FSS_CSS_ANGLE_DIFF)            

    # Solar Array Angles -----------------------------
    #
    plot_ltt('AOSARES1', **plot_AOSARES1)               
    plot_ltt('AOSARES2', **plot_AOSARES2)               
    
    # IRU-1 ------------------------------------------
    if Time.DateTime(start) < Time.DateTime('2003:200'):
        if Time.DateTime(stop) > Time.DateTime('2003:200'):
            stop_iru1 = '2003:199'
        else:  
            stop_iru1 = stop
        #
        plot_ltt('AIRU1G1I', **plot_AIRU1G1I)              
        plot_ltt('AIRU1G2I', **plot_AIRU1G2I)              
        #
        plot_ltt('AIRU1G1T', **plot_AIRU1G1T)              
        plot_ltt('AIRU1G2T', **plot_AIRU1G2T)              
        #
        plot_ltt('AIRU1BT', **plot_AIRU1BT)                
        plot_ltt('AIRU1VFT', **plot_AIRU1VFT)              

    # IRU-2 ------------------------------------------
    if Time.DateTime(stop) > Time.DateTime('2003:201'):
        if Time.DateTime(start) < Time.DateTime('2003:201'):
            start_iru1 = '2003:201'
        else:  
            start_iru1 = start
        #
        plot_ltt('AIRU2G1I', **plot_AIRU2G1I)              
        plot_ltt('AIRU2G2I', **plot_AIRU2G2I)              
        #
        plot_ltt('AIRU2G1T', **plot_AIRU2G1T)              
        plot_ltt('AIRU2G2T', **plot_AIRU2G2T)              
        #
        plot_ltt('AIRU2BT', **plot_AIRU2BT)                
        plot_ltt('AIRU2VFT', **plot_AIRU2VFT)              

    # IRU Biases -------------------------------------
    #
    plot_ltt('AOGBIAS1', **plot_AOGBIAS1)                
    plot_ltt('AOGBIAS2', **plot_AOGBIAS2)                
    plot_ltt('AOGBIAS3', **plot_AOGBIAS3)                

    # RW Speeds --------------------------------------
    #
    plot_ltt('AORWSPD1', **plot_AORWSPD1)                
    plot_ltt('AORWSPD2', **plot_AORWSPD2)                
    plot_ltt('AORWSPD3', **plot_AORWSPD3)                
    #
    plot_ltt('AORWSPD4', **plot_AORWSPD4)                
    plot_ltt('AORWSPD5', **plot_AORWSPD5)                
    plot_ltt('AORWSPD6', **plot_AORWSPD6)                

    # RW Compartment Temperatures ------------------------
    plot_ltt('TCYZ_RW1', **plot_TCYZ_RW1)                
    plot_ltt('TPCP_RW2', **plot_TPCP_RW2)                
    plot_ltt('TPCP_RW3', **plot_TPCP_RW3)                
    #
    plot_ltt('TPCM_RW4', **plot_TPCM_RW4)                
    plot_ltt('TPCM_RW5', **plot_TPCM_RW5)                
    plot_ltt('TCYZ_RW6', **plot_TCYZ_RW6)                

    # RW Bearing Temperatures ------------------------
    plot_ltt('ARWA1BT', **plot_ARWA1BT)                 
    plot_ltt('ARWA2BT', **plot_ARWA2BT)                 
    plot_ltt('ARWA3BT', **plot_ARWA3BT)                 
    #
    plot_ltt('ARWA4BT', **plot_ARWA4BT)                 
    plot_ltt('ARWA5BT', **plot_ARWA5BT)                 
    plot_ltt('ARWA6BT', **plot_ARWA6BT)                 

    # RW Delta (Compartment - Bearing) Temperatures ------
    plot_ltt('DP_RW1_DELTA_TEMP', **plot_DP_RW1_DELTA_TEMP)
    plot_ltt('DP_RW2_DELTA_TEMP', **plot_DP_RW2_DELTA_TEMP)
    plot_ltt('DP_RW3_DELTA_TEMP', **plot_DP_RW3_DELTA_TEMP)
    #
    plot_ltt('DP_RW4_DELTA_TEMP', **plot_DP_RW4_DELTA_TEMP)
    plot_ltt('DP_RW5_DELTA_TEMP', **plot_DP_RW5_DELTA_TEMP)
    plot_ltt('DP_RW6_DELTA_TEMP', **plot_DP_RW6_DELTA_TEMP)

    # RW Torque Currents -----------------------------
    #
    plot_ltt('AWD1TQI', **plot_AWD1TQI)                 
    plot_ltt('AWD2TQI', **plot_AWD2TQI)                 
    plot_ltt('AWD3TQI', **plot_AWD3TQI)                 
    #
    plot_ltt('AWD4TQI', **plot_AWD4TQI)                 
    plot_ltt('AWD5TQI', **plot_AWD5TQI)                 
    plot_ltt('AWD6TQI', **plot_AWD6TQI)                 

    # RW Drag Torque ---------------------------------
    #
    plot_ltt('AORWCMD1', **plot_AORWCMD1)               
    plot_ltt('AORWCMD2', **plot_AORWCMD2)               
    plot_ltt('AORWCMD3', **plot_AORWCMD3)               
    #
    plot_ltt('AORWCMD4', **plot_AORWCMD4)               
    plot_ltt('AORWCMD5', **plot_AORWCMD5)               
    plot_ltt('AORWCMD6', **plot_AORWCMD6)               
       
    # WDE Converter Voltages -------------------------
    #
    plot_ltt('AWD1CV5V', **plot_AWD1CV5V)               
    plot_ltt('AWD2CV5V', **plot_AWD2CV5V)               
    plot_ltt('AWD3CV5V', **plot_AWD3CV5V)               
    #
    plot_ltt('AWD4CV5V', **plot_AWD4CV5V)               
    plot_ltt('AWD5CV5V', **plot_AWD5CV5V)               
    plot_ltt('AWD6CV5V', **plot_AWD6CV5V)               

    # Other Converter Voltages -----------------------
    #
    plot_ltt('ACPA5CV', **plot_ACPA5CV)           
    plot_ltt('ADE1P5CV', **plot_ADE1P5CV)         
    plot_ltt('AFSSPC1V', **plot_AFSSPC1V)         
    #
    plot_ltt('AGWS1V', **plot_AGWS1V)             
    plot_ltt('AGWS2V', **plot_AGWS2V)             
    plot_ltt('AIOAP5CV', **plot_AIOAP5CV)         
    #
    plot_ltt('ASPEA5CV', **plot_ASPEA5CV)               
    plot_ltt('AVD1CV5V', **plot_AVD1CV5V)               

    # EPIC Register Mismatches & CPE Error Count ------
    #
    plot_ltt('AOEPICER', **plot_AOEPICER)               
    plot_ltt('AOCPESTC', **plot_AOCPESTC)               

   
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
#plot_ltt(temp,2)
# PITCH_CTRL, MEAN PITCH POINTING CONTROL, ARCSEC, MEAN
# YAW_CTRL, MEAN YAW POINTING CONTROL, ARCSEC, MEAN
# PITCH_STAB, PITCH_STAB, ARCSEC, MEAN
# YAW_STAB, YAW_STAB, ARCSEC, MEAN