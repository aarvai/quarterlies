from os import chdir, mkdir, path

from Chandra import Time

import pcad_plots as pcad

##-------------------------------------------------------------
# Define Custom LTT Plots

def pcad_ltts(start, stop):

    # ACA --------------------------------------------
    #
    plot_ltt('aacccdpt', **pcad.plot_aacccdpt)
    plot_ltt('aflcaah', **pcad.plot_aflcaah)

    # Min CSS Counts in NPM, Sun ---------------------
    plot_ltt('dp_css1_npm_sun', **pcad.plot_dp_css1_npm_sun)
    plot_ltt('dp_css2_npm_sun', **pcad.plot_dp_css2_npm_sun)
    plot_ltt('dp_css3_npm_sun', **pcad.plot_dp_css3_npm_sun)
    plot_ltt('dp_css4_npm_sun', **pcad.plot_dp_css4_npm_sun)  
    
    # FSS Angles -------------------------------------
    #
    plot_ltt('dp_roll_fss', **pcad.plot_dp_roll_fss)          
    plot_ltt('dp_pitch_fss', **pcad.plot_dp_pitch_fss)        
    #
    plot_ltt('aoalpang', **pcad.plot_aoalpang)                
    plot_ltt('aobetang', **pcad.plot_aobetang)                

    # FSS / CSS Sun Vector Difference ----------------
    plot_ltt('dp_fss_css_angle_diff', **pcad.plot_dp_fss_css_angle_diff)            

    # Solar Array Angles -----------------------------
    #
    plot_ltt('aosares1', **pcad.plot_aosares1)               
    plot_ltt('aosares2', **pcad.plot_aosares2)               
    
    # IRU-1 ------------------------------------------
    if Time.DateTime(start) < Time.DateTime('2003:200'):
        if Time.DateTime(stop) > Time.DateTime('2003:200'):
            stop_iru1 = '2003:199'
        else:  
            stop_iru1 = stop
        #
        plot_ltt('airu1g1i', **pcad.plot_airu1g1i)              
        plot_ltt('airu1g2i', **pcad.plot_airu1g2i)              
        #
        plot_ltt('airu1g1t', **pcad.plot_airu1g1t)              
        plot_ltt('airu1g2t', **pcad.plot_airu1g2t)              
        #
        plot_ltt('airu1bt', **pcad.plot_airu1bt)                
        plot_ltt('airu1vft', **pcad.plot_airu1vft)              

    # IRU-2 ------------------------------------------
    if Time.DateTime(stop) > Time.DateTime('2003:201'):
        if Time.DateTime(start) < Time.DateTime('2003:201'):
            start_iru1 = '2003:201'
        else:  
            start_iru1 = start
        #
        plot_ltt('airu2g1i', **pcad.plot_airu2g1i)              
        plot_ltt('airu2g2i', **pcad.plot_airu2g2i)              
        #
        plot_ltt('airu2g1t', **pcad.plot_airu2g1t)              
        plot_ltt('airu2g2t', **pcad.plot_airu2g2t)              
        #
        plot_ltt('airu2bt', **pcad.plot_airu2bt)                
        plot_ltt('airu2vft', **pcad.plot_airu2vft)              

    # IRU Biases -------------------------------------
    #
    plot_ltt('aogbias1', **pcad.plot_aogbias1)                
    plot_ltt('aogbias2', **pcad.plot_aogbias2)                
    plot_ltt('aogbias3', **pcad.plot_aogbias3)                

    # RW Speeds --------------------------------------
    #
    plot_ltt('aorwspd1', **pcad.plot_aorwspd1)                
    plot_ltt('aorwspd2', **pcad.plot_aorwspd2)                
    plot_ltt('aorwspd3', **pcad.plot_aorwspd3)                
    #
    plot_ltt('aorwspd4', **pcad.plot_aorwspd4)                
    plot_ltt('aorwspd5', **pcad.plot_aorwspd5)                
    plot_ltt('aorwspd6', **pcad.plot_aorwspd6)                

    # RW Compartment Temperatures ------------------------
    plot_ltt('tcyz_rw1', **pcad.plot_tcyz_rw1)                
    plot_ltt('tpcp_rw2', **pcad.plot_tpcp_rw2)                
    plot_ltt('tpcp_rw3', **pcad.plot_tpcp_rw3)                
    #
    plot_ltt('tpcm_rw4', **pcad.plot_tpcm_rw4)                
    plot_ltt('tpcm_rw5', **pcad.plot_tpcm_rw5)                
    plot_ltt('tcyz_rw6', **pcad.plot_tcyz_rw6)                

    # RW Bearing Temperatures ------------------------
    plot_ltt('arwa1bt', **pcad.plot_arwa1bt)                 
    plot_ltt('arwa2bt', **pcad.plot_arwa2bt)                 
    plot_ltt('arwa3bt', **pcad.plot_arwa3bt)                 
    #
    plot_ltt('arwa4bt', **pcad.plot_arwa4bt)                 
    plot_ltt('arwa5bt', **pcad.plot_arwa5bt)                 
    plot_ltt('arwa6bt', **pcad.plot_arwa6bt)                 

    # RW Delta (Compartment - Bearing) Temperatures ------
    plot_ltt('dp_rw1_delta_temp', **pcad.plot_dp_rw1_delta_temp)
    plot_ltt('dp_rw2_delta_temp', **pcad.plot_dp_rw2_delta_temp)
    plot_ltt('dp_rw3_delta_temp', **pcad.plot_dp_rw3_delta_temp)
    #
    plot_ltt('dp_rw4_delta_temp', **pcad.plot_dp_rw4_delta_temp)
    plot_ltt('dp_rw5_delta_temp', **pcad.plot_dp_rw5_delta_temp)
    plot_ltt('dp_rw6_delta_temp', **pcad.plot_dp_rw6_delta_temp)

    # RW Torque Currents -----------------------------
    #
    plot_ltt('awd1tqi', **pcad.plot_awd1tqi)                 
    plot_ltt('awd2tqi', **pcad.plot_awd2tqi)                 
    plot_ltt('awd3tqi', **pcad.plot_awd3tqi)                 
    #
    plot_ltt('awd4tqi', **pcad.plot_awd4tqi)                 
    plot_ltt('awd5tqi', **pcad.plot_awd5tqi)                 
    plot_ltt('awd6tqi', **pcad.plot_awd6tqi)                 

    # RW Drag Torque ---------------------------------
    #
    plot_ltt('aorwcmd1', **pcad.plot_aorwcmd1)               
    plot_ltt('aorwcmd2', **pcad.plot_aorwcmd2)               
    plot_ltt('aorwcmd3', **pcad.plot_aorwcmd3)               
    #
    plot_ltt('aorwcmd4', **pcad.plot_aorwcmd4)               
    plot_ltt('aorwcmd5', **pcad.plot_aorwcmd5)               
    plot_ltt('aorwcmd6', **pcad.plot_aorwcmd6)               
       
    # WDE Converter Voltages -------------------------
    #
    plot_ltt('awd1cv5v', **pcad.plot_awd1cv5v)               
    plot_ltt('awd2cv5v', **pcad.plot_awd2cv5v)               
    plot_ltt('awd3cv5v', **pcad.plot_awd3cv5v)               
    #
    plot_ltt('awd4cv5v', **pcad.plot_awd4cv5v)               
    plot_ltt('awd5cv5v', **pcad.plot_awd5cv5v)               
    plot_ltt('awd6cv5v', **pcad.plot_awd6cv5v)               

    # Other Converter Voltages -----------------------
    #
    plot_ltt('acpa5cv', **pcad.plot_acpa5cv)           
    plot_ltt('ade1p5cv', **pcad.plot_ade1p5cv)         
    plot_ltt('afsspc1v', **pcad.plot_afsspc1v)         
    #
    plot_ltt('agws1v', **pcad.plot_agws1v)             
    plot_ltt('agws2v', **pcad.plot_agws2v)             
    plot_ltt('aioap5cv', **pcad.plot_aioap5cv)         
    #
    plot_ltt('aspea5cv', **pcad.plot_aspea5cv)               
    plot_ltt('avd1cv5v', **pcad.plot_avd1cv5v)               

    # EPIC Register Mismatches & CPE Error Count ------
    #
    plot_ltt('aoepicer', **pcad.plot_aoepicer)               
    plot_ltt('aocpestc', **pcad.plot_aocpestc)               

   
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