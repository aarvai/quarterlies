from os import chdir, mkdir, path
from matplotlib import pyplot as pp

from Chandra import Time

import ltt
import pcad_plots
import prop_plots

##-------------------------------------------------------------
# Inputs

start = '2011:212:00:00:00'
stop = '2012:031:00:00:00'

##-------------------------------------------------------------
# Utilities
def mkdir_cd(dir):
    # Make a directory (if doesn't already exist) and cd to it.
    if not path.exists(dir):
        mkdir(dir)
    chdir(dir) 

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
mkdir_cd('../quarter')
ltt.pcad_ltts(start, stop)
mkdir_cd('../../' + prop_dir)
mkdir_cd('mission')
ltt.prop_ltts('2002:001:00:00:00', stop)
mkdir_cd('zoom')
ltt.prop_zoom_ltts('2002:001:00:00:00', stop)
mkdir_cd('../../other')
prop_plots.mups_tank(stop)
prop_plots.therm_dropouts(stop)
chdir('../..')
pp.close('all')


