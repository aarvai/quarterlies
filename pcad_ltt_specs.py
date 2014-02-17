from math import pi

plot_aacccdpt =              {'plot_limits': False, 
                              'subplot': [2,1,1], 
                              'savefig': False}
		       
plot_acpa5cv  =              {'plot_limits': False, 
                              'subplot': [3,1,1], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN CPE-A +5V CONVERTER VOLTAGE - ACPA5CV', 
                              'savefig': False}
		       
plot_ade1p5cv =              {'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN ADE-A +5V CONVERTER VOLTAGE - ADE1P5CV', 
                              'samefig': True, 
                              'savefig': False}   
		             
plot_aflcaah =               {'plot_limits': False, 
                              'cust_title': 'FLCA SOH - AFLCAAH', 
                              'subplot': [2,1,2], 
                              'samefig': True, 
                              'saveas': '01_ACA_TEMP_SOH.png'}
		       
plot_afsspc1v =              {'ylim': [3.495, 3.530],
                              'plot_limits': False, 
                              'subplot': [3,1,1], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN FSS-A +5V CONVERTER VOLTAGE - AFSSPC1V', 
                              'savefig': False} 

plot_afsspc2v =              {'ylim': [3.495, 3.530],
                              'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN FSS-B +5V CONVERTER VOLTAGE - AFSSPC2V', 
                              'samefig': True, 
                              'saveas': '34_CONV_VOLT_FSS.png'} 
		        
plot_agws1v =                {'plot_limits': False, 
                              'subplot': [3,1,1], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN GYRO WHEEL SUPPLY 1 INPUT VOLTAGE - AGWS1V', 
                              'savefig': False}
		       
plot_agws2v =                {'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN GYRO WHEEL SUPPLY 2 INPUT VOLTAGE - AGWS2V', 
                              'samefig': True, 
                              'savefig': False}
		       
plot_aioap5cv =              {'plot_limits': False, 
                              'subplot': [3,1,3], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN IOE-A +5V CONVERTER VOLTAGE - AIOAP5CV', 
                              'samefig': True, 
                              'saveas': '05_CONV_VOLT_OTHER_2.png'}   
		        
plot_airu1g1i =              {'plot_limits': False, 
                              'subplot': [2,1,1], 
                              'savefig': False}
		        
plot_airu1g2i =              {'plot_limits': False, 
                              'subplot': [2,1,2], 
                              'samefig': True, 
                              'saveas': '07_IRU_1_CURRENTS.png'}
		       
plot_airu1g1t =              {'plot_limits': False, 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN IRU-1 GYRO #1 TEMP - AIRU1G1T', 
                              'subplot': [2,1,1], 
                              'savefig': False}
		       
plot_airu1g2t =              {'plot_limits': False, 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN IRU-1 GYRO #2 TEMP - AIRU1G2T', 
                              'subplot': [2,1,2], 
                              'samefig': True, 
                              'saveas': '08_IRU_1_TEMPS_1.png'}

plot_airu1bt =               {'plot_limits': False, 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN IRU-1 BASE TEMPERATURE - AIRU1BT', 
                              'subplot': [2,1,1], 
                              'savefig': False}

plot_airu1vft =              {'plot_limits': False, 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN IRU-1 VFC TEMPERATURE - AIRU1VFT', 
                              'subplot': [2,1,2], 
                              'samefig': True, 
                              'saveas': '09_IRU_1_TEMPS_2.png'}

plot_airu2g1i =              {'plot_limits': False, 
                              'subplot': [2,1,1], 
                              'savefig': False}
		       
plot_airu2g2i =              {'plot_limits': False, 
                              'subplot': [2,1,2], 
                              'samefig': True, 
                              'saveas': '10_IRU_2_CURRENTS.png'}
		      
plot_airu2g1t =              {'plot_limits': False, 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN IRU-2 GYRO #1 TEMP - AIRU2G1T', 
                              'subplot': [2,1,1], 
                              'savefig': False}
		       
plot_airu2g2t =              {'plot_limits': False, 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN IRU-2 GYRO #2 TEMP - AIRU2G2T', 
                              'subplot': [2,1,2], 
                              'samefig': True, 
                              'saveas': '11_IRU_2_TEMPS_1.png'}

plot_airu2bt =               {'plot_limits': False, 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN IRU-2 BASE TEMPERATURE - AIRU2BT', 
                              'subplot': [2,1,1], 
                              'savefig': False}
		             
plot_airu2vft =              {'plot_limits': False, 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN IRU-2 VFC TEMPERATURE - AIRU2VFT', 
                              'subplot': [2,1,2], 
                              'samefig': True, 
                              'saveas': '12_IRU_2_TEMPS_2.png'}
		             
plot_aoalpang =              {'plot_limits': False, 
                              'subplot': [2,1,1], 
                              'savefig': False}
		             
plot_aoatter2 =              {'plot_limits': False,
                              'plot_mins': False,
                              'plot_maxes': False,
                              'cust_unit': 'ARCSEC',
                              'cust_mult': 3600 * 180 / pi,
                              'cust_title': 'MEAN PITCH POINTING CONTROL - AOATTER2',
                              'subplot': [2,1,1],
                              'savefig': False}

plot_aoatter3 =              {'plot_limits': False,
                              'plot_mins': False,
			      'plot_maxes': False,
			      'cust_unit': 'ARCSEC',
			      'cust_mult': 3600 * 180 / pi,
                              'cust_title': 'MEAN YAW POINTING CONTROL - AOATTER3',
                              'subplot': [2,1,2],
                              'samefig': True,
                              'saveas': '33_POINTING_CONTROL.png'}                              

plot_aobetang =              {'plot_limits': False, 
                              'subplot': [2,1,2], 
                              'samefig': True, 
                              'saveas': '17_FSS_ALPHA_BETA.png'}
		             
plot_aocpestc =              {'plot_limits': False, 
                              'subplot': [2,1,2], 
                              'cust_title': 'CPE ERROR COUNT - AOCPESTC', 
                              'samefig': True, 
                              'saveas': '13_EPIC_CPE.png'} 
		             
plot_aoepicer =              {'plot_limits': False, 
                              'plot_stds': False, 
                              'subplot': [2,1,1], 
                              'savefig': False}
		             
plot_aogbias1 =              {'plot_limits': False, 
                              'cust_unit': 'ARCSEC/SEC', 
                              'cust_mult': 3600*180/pi, 
                              'subplot': [3,1,1], 
                              'savefig': False}

plot_aogbias2 =              {'plot_limits': False, 
                              'cust_unit': 'ARCSEC/SEC', 
                              'cust_mult': 3600*180/pi, 
                              'subplot': [3,1,2], 
                              'samefig': True, 
                              'savefig': False}
		             
plot_aogbias3 =              {'plot_limits': False, 
                              'cust_unit': 'ARCSEC/SEC', 
                              'cust_mult': 3600*180/pi, 
                              'subplot': [3,1,3], 
                              'samefig': True, 
                              'saveas': '28_IRU_GRYO_BIASES.png'}
		             
plot_aorwcmd1 =              {'plot_limits': False, 
                              'subplot': [3,1,1], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN RW #1 COMMANDED TORQUE - AORWCMD1', 
                              'savefig': False}
		             
plot_aorwcmd2 =              {'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN RW #2 COMMANDED TORQUE - AORWCMD2', 
                              'samefig': True, 
                              'savefig': False}  

plot_aorwcmd3 =              {'plot_limits': False, 
                              'subplot': [3,1,3], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN RW #3 COMMANDED TORQUE - AORWCMD3', 
                              'samefig': True, 
                              'saveas': '14_RW_CMD_TORQUE_1.png'}   
		             
plot_aorwcmd4 =              {'plot_limits': False, 
                              'subplot': [3,1,1], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN RW #4 COMMANDED TORQUE - AORWCMD4', 
                              'savefig': False}

plot_aorwcmd5 =              {'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN RW #5 COMMANDED TORQUE - AORWCMD5', 
                              'samefig': True, 
                              'savefig': False}  

plot_aorwcmd6 =              {'plot_limits': False, 
                              'subplot': [3,1,3], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN RW #6 COMMANDED TORQUE - AORWCMD6', 
                              'samefig': True, 
                              'saveas': '15_RW_CMD_TORQUE_2.png'}      

plot_aorwspd1 =              {'plot_limits': False, 
                              'cust_unit': 'RPM', 
                              'cust_mult': 60 / (2 * pi), 
                              'subplot': [3,1,1], 
                              'savefig': False}

plot_aorwspd2 =              {'plot_limits': False, 
                              'cust_unit': 'RPM', 
                              'cust_mult': 60 / (2 * pi), 
                              'subplot': [3,1,2], 
                              'samefig': True, 
                              'savefig': False}

plot_aorwspd3 =              {'plot_limits': False, 
                              'cust_unit': 'RPM', 
                              'cust_mult': 60 / (2 * pi), 
                              'subplot': [3,1,3], 
                              'samefig': True, 
                              'saveas': '02_RW_SPEEDS_1.png'}    

plot_aorwspd4 =              {'plot_limits': False, 
                              'cust_unit': 'RPM', 
                              'cust_mult': 60 / (2 * pi), 
                              'subplot': [3,1,1], 
                              'savefig': False}

plot_aorwspd5 =              {'plot_limits': False, 
                              'cust_unit': 'RPM', 
                              'cust_mult': 60 / (2 * pi), 
                              'subplot': [3,1,2], 
                              'samefig': True, 
                              'savefig': False}

plot_aorwspd6 =              {'plot_limits': False, 
                              'cust_unit': 'RPM', 
                              'cust_mult': 60 / (2 * pi), 
                              'subplot': [3,1,3], 
                              'samefig': True, 
                              'saveas': '03_RW_SPEEDS_2.png'}    

plot_aosares1 =              {'plot_limits': False, 
                              'subplot': [2,1,1], 
                              'savefig': False}

plot_aosares2 =              {'plot_limits': False, 
                              'subplot': [2,1,2], 
                              'samefig': True, 
                              'saveas': '16_SA_RES_ANGLES.png'}

plot_arwa1bt=                {'plot_limits': False, 
                              'subplot': [3,1,1], 
                              'savefig': False}

plot_arwa2bt=                {'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'samefig': True, 
                              'savefig': False}

plot_arwa3bt=                {'plot_limits': False, 
                              'subplot': [3,1,3], 
                              'samefig': True, 
                              'saveas': '18_RW_BEARING_TEMPS_1.png'}    

plot_arwa4bt=                {'plot_limits': False, 
                              'subplot': [3,1,1], 
                              'savefig': False}

plot_arwa5bt=                {'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'samefig': True, 
                              'savefig': False}

plot_arwa6bt=                {'plot_limits': False, 
                              'subplot': [3,1,3], 
                              'samefig': True, 
                              'saveas': '19_RW_BEARING_TEMPS_2.png'}      

plot_aspea5cv =              {'plot_limits': False, 
                              'subplot': [3,1,3], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN SPE-A +5V CONVERTER VOLTAGE - ASPEA5CV', 
                              'samefig': True,
                              'saveas': '04_CONV_VOLT_OTHER_1.png'} 

plot_avd1cv5v =              {'plot_limits': False, 
                              'subplot': [3,1,1], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN VDE-A +5V CONVERTER VOLTAGE - AVD1CV5V', 
                              'savefig': False}    

plot_avd2cv5v =              {'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN VDE-B +5V CONVERTER VOLTAGE - AVD2CV5V', 
                              'samefig': True, 
                              'saveas': '06_CONV_VOLT_VDE.png'}                                 

plot_awd1cv5v =              {'plot_limits': False, 
                              'subplot': [3,1,1], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN WDE-1 +5V CONVERTER VOLTAGE - AWD1CV5V', 
                              'savefig': False}

plot_awd2cv5v =              {'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN WDE-2 +5V CONVERTER VOLTAGE - AWD2CV5V', 
                              'samefig': True, 
                              'savefig': False}   

plot_awd3cv5v =              {'ylim': [5.28, 5.33],
                              'plot_limits': False, 
                              'subplot': [3,1,3], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN WDE-3 +5V CONVERTER VOLTAGE - AWD3CV5V', 
                              'samefig': True, 
                              'saveas': '26_CONV_VOLT_WDE_1.png'} 

plot_awd4cv5v =              {'plot_limits': False, 
                              'subplot': [3,1,1], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN WDE-4 +5V CONVERTER VOLTAGE - AWD4CV5V', 
                              'savefig': False}

plot_awd5cv5v =              {'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN WDE-5 +5V CONVERTER VOLTAGE - AWD5CV5V', 
                              'samefig': True, 
                              'savefig': False}   

plot_awd6cv5v =              {'plot_limits': False, 
                              'subplot': [3,1,3], 
                              'plot_mins': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MEAN WDE-6 +5V CONVERTER VOLTAGE - AWD6CV5V', 
                              'samefig': True, 
                              'saveas': '27_CONV_VOLT_WDE_2.png'} 

plot_awd1tqi =               {'plot_limits': False, 
                              'subplot': [3,1,1], 'savefig': False}

plot_awd2tqi =               {'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'samefig': True, 
                              'savefig': False}

plot_awd3tqi =               {'plot_limits': False, 
                              'subplot': [3,1,3], 
                              'samefig': True, 
                              'saveas': '20_RW_TORQUE_CURR_1.png'}    

plot_awd4tqi =               {'plot_limits': False, 
                              'subplot': [3,1,1], 
                              'savefig': False}

plot_awd5tqi =               {'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'samefig': True, 
                              'savefig': False}

plot_awd6tqi =               {'plot_limits': False, 
                              'subplot': [3,1,3], 
                              'samefig': True, 
                              'saveas': '21_RW_TORQUE_CURR_2.png'}  

plot_dp_css1_npm_sun =       {'plot_limits': False, 
                              'plot_means': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MIN CSS-1 COUNTS IN NPM ONLY', 
                              'cust_unit': 'COUNTS', 
                              'subplot': [4,1,1], 
                              'savefig': False}

plot_dp_css2_npm_sun =       {'plot_limits': False, 
                              'plot_means': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MIN CSS-2 COUNTS IN NPM ONLY', 
                              'cust_unit': 'COUNTS', 'subplot': [4,1,2], 
                              'samefig': True, 
                              'savefig': False}

plot_dp_css3_npm_sun =       {'plot_limits': False, 
                              'plot_means': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MIN CSS-3 COUNTS IN NPM ONLY', 
                              'cust_unit': 'COUNTS', 
                              'subplot': [4,1,3], 
                              'samefig': True, 
                              'savefig': False}

plot_dp_css4_npm_sun =       {'plot_limits': False, 
                              'plot_means': False, 
                              'plot_maxes': False, 
                              'cust_title': 'MIN CSS-4 COUNTS IN NPM ONLY', 
                              'cust_unit': 'COUNTS', 
                              'subplot': [4,1,4], 
                              'samefig': True, 
                              'saveas': '29_MIN_CSS_COUNTS.png'}      

plot_dp_fss_css_angle_diff = {'plot_limits': False, 
                              'cust_unit': 'DEG', 
                              'saveas': '30_FSS_CSS_ANGLE_DIFF.png'}

plot_dp_pitch_fss =          {'cust_title': 'FSS PITCH ANGLE', 
                              'cust_unit': 'DEG', 
                              'plot_limits': False, 
                              'samefig': True, 
                              'subplot': [2,1,2], 
                              'saveas': '18_FSS_ROLL_PITCH.png'}

plot_dp_roll_fss =           {'cust_title': 'FSS ROLL ANGLE', 
                              'cust_unit': 'DEG', 
                              'plot_limits': False, 
                              'subplot': [2,1,1], 
                              'savefig': False}

plot_dp_rw1_delta_temp =     {'plot_limits': False, 
                              'cust_title': 'RW-1 COMP - BEARING TEMP  = {TCYZ_RW1 - ARWA1BT}', 
                              'cust_unit': 'DEG F', 
                              'subplot': [3,1,1], 
                              'savefig': False}

plot_dp_rw2_delta_temp =     {'plot_limits': False, 
                              'cust_title': 'RW-2 COMP - BEARING TEMP  = {TPCP_RW2 - ARWA1BT}', 
                              'cust_unit': 'DEG F', 
                              'subplot': [3,1,2], 
                              'samefig': True, 
                              'savefig': False}

plot_dp_rw3_delta_temp =     {'plot_limits': False, 
                              'cust_title': 'RW-3 COMP - BEARING TEMP  = {TPCP_RW3 - ARWA1BT}', 
                              'cust_unit': 'DEG F', 
                              'subplot': [3,1,3], 
                              'samefig': True, 
                              'saveas': '24_RW_DELTA_TEMPS_1.png'}    

plot_dp_rw4_delta_temp =     {'plot_limits': False, 
                              'cust_title': 'RW-4 COMP - BEARING TEMP  = {TPCM_RW4 - ARWA1BT}', 
                              'cust_unit': 'DEG F', 
                              'subplot': [3,1,1], 
                              'savefig': False}

plot_dp_rw5_delta_temp =     {'plot_limits': False, 
                              'cust_title': 'RW-5 COMP - BEARING TEMP  = {TPCM_RW5 - ARWA1BT}', 
                              'cust_unit': 'DEG F', 
                              'subplot': [3,1,2], 
                              'samefig': True, 
                              'savefig': False}

plot_dp_rw6_delta_temp =     {'plot_limits': False, 
                              'cust_title': 'RW-6 COMP - BEARING TEMP  = {TCYZ_RW6 - ARWA1BT}', 
                              'cust_unit': 'DEG F', 
                              'subplot': [3,1,3], 
                              'samefig': True, 
                              'saveas': '25_RW_DELTA_TEMPS_2.png'}      

plot_tcyz_rw1 =              {'plot_limits': False, 
                              'subplot': [3,1,1], 
                              'savefig': False}

plot_tpcp_rw2 =              {'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'samefig': True, 
                              'savefig': False}

plot_tpcp_rw3 =              {'plot_limits': False, 
                              'subplot': [3,1,3], 
                              'samefig': True, 
                              'saveas': '22_RW_COMP_TEMPS_1.png'}    

plot_tpcm_rw4 =              {'plot_limits': False, 
                              'subplot': [3,1,1], 
                              'savefig': False}

plot_tpcm_rw5 =              {'plot_limits': False, 
                              'subplot': [3,1,2], 
                              'samefig': True, 
                              'savefig': False}

plot_tcyz_rw6 =              {'plot_limits': False, 
                              'subplot': [3,1,3], 
                              'samefig': True, 
                              'saveas': '23_RW_COMP_TEMPS_2.png'}      