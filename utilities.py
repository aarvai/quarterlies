import numpy as np
from os import chdir, mkdir, path
from matplotlib import pyplot as pp

from os import mkdir, chdir

def mkdir_cd(dir):
    # Make a directory (if doesn't already exist) and cd to it.
    if not path.exists(dir):
        mkdir(dir)
    chdir(dir) 

def smaller_axes(ax1):
    # Replace existing axes with one only 90% width and 75% height, 
    # allowing more room for ticks and titles
    ax_pos = ax1.get_position().get_points()
    ax_width = ax_pos[1,0] - ax_pos[0,0]
    ax_height = ax_pos[1,1] - ax_pos[0,1]
    pp.delaxes(ax1)
    ax2 = pp.axes([ax_pos[0,0] + .10 * ax_width, ax_pos[0,1] + .20 * ax_height, 
                  .90 * ax_width, .75 * ax_height])  
    return ax2

def reshape_array(array, num_rows, order='F'):
    # Return an array based on the values of the input array, but reshaped
    # with a user-specified number of rows.  Excess data will be trucated.
    #
    # Order = 'F' (column-major, FORTRAN-style)
    #       = 'C' (row-major, C-style)
    if np.mod(len(array),num_rows) > 0:
        out = array[:-np.mod(len(array), num_rows)].reshape((num_rows, np.floor(len(array) / int(num_rows))), order=order)
    else:
        out = array.reshape((num_rows, len(stdev) / int(num_rows)), order=order)
    return out

    