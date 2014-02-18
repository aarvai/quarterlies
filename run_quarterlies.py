from matplotlib import pyplot as pp
from os import chdir

from Chandra import Time

import ltt
import pcad_plots
import prop_plots
from utilities import mkdir_cd 

##-------------------------------------------------------------
# Inputs - Quarter start and stop

start = '2013:213:00:00:00'
stop = '2014:031:00:00:00'

##-------------------------------------------------------------
# Run Quarterlies

# Define directory names
t = Time.DateTime()
new_dir = t.date[:4] + '_' + t.date[5:8] + '_RUN'
pcad_dir = 'pcad_' + t.date[:4] + '_' + t.date[5:8]
prop_dir = 'prop_' + t.date[:4] + '_' + t.date[5:8]

# Make directories and create plots
pp.close('all')
mkdir_cd(new_dir)
mkdir_cd(pcad_dir)
mkdir_cd('mission')
ltt.pcad_ltts('2000:001', stop)
pcad_plots.fss('2000:001', stop)
#pcad_plots.pointing_stab('pitch', '2000:001:00:00:00', stop)
#pcad_plots.pointing_stab('yaw', '2000:001:00:00:00', stop)
#pcad_plots.cmd_vs_act_torque('2000:001', stop)
pcad_plots.drag_torque('2000:001', stop, plot_months=False)
mkdir_cd('../quarter')
ltt.pcad_ltts(start, stop)
pcad_plots.fss(start, stop)
#pcad_plots.pointing_stab('pitch', start, stop)
#pcad_plots.pointing_stab('yaw', start, stop)
#pcad_plots.cmd_vs_act_torque(start, stop)
mkdir_cd('../../' + prop_dir)
mkdir_cd('mission')
ltt.prop_ltts('2002:001:00:00:00', stop)
prop.htr_dc('PM3THV2T', on_temp=60, off_temp=89) 
mkdir_cd('zoom')
ltt.prop_zoom_ltts('2002:001:00:00:00', stop)
mkdir_cd('../../other')
prop_plots.mups_tank(stop)
prop_plots.therm_dropouts(stop)
chdir('../..')
pp.close('all')
pcad_plots.collect_bias_data(stop) #this step adds ~10 min


