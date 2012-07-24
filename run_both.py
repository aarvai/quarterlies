from os import chdir, mkdir, path
from matplotlib import pyplot as pp

from Chandra import Time

from ltt import plot_ltt
import pcad_plots as pcad

##-------------------------------------------------------------
# Inputs

start = '2011:212:00:00:00'
stop = '2012:031:00:00:00'


##-------------------------------------------------------------
# Run Quarterlies

pp.close('all')

t = Time.DateTime()
new_dir = t.date[:4] + '_' + t.date[5:8] + '_RUN'
pcad_dir = 'pcad_' + t.date[:4] + '_' + t.date[5:8]
prop_dir = 'prop_' + t.date[:4] + '_' + t.date[5:8]

if not path.exists(new_dir):
    mkdir(new_dir)
chdir(new_dir)

if not path.exists(pcad_dir):
    mkdir(pcad_dir)
chdir(pcad_dir)
#execfile('/home/aarvai/python/quarterlies/pcad_quarterly.py')
chdir('..')

if not path.exists(prop_dir):
    mkdir(prop_dir)
chdir(prop_dir)
execfile('/home/aarvai/python/quarterlies/prop_quarterly.py')
chdir('../..')
pp.close('all')
