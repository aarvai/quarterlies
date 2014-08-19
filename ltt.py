import numpy as np
from matplotlib import pyplot as pp
from matplotlib import ticker

from Ska.engarchive import fetch_eng as fetch
from Ska.Matplotlib import plot_cxctime
from Chandra import Time

import filter_times as bad
import pcad_ltt_specs as pcad
import prop_ltt_specs as prop

##-------------------------------------------------------------
# Long term trending plotting function

def plot_ltt(var, **kwargs): 
    """Plot the daily min, max, and mean of a parameter, filtering for known
    bad data as listed in filter_times.py.
    
    :var:  MSID or derived parameter name (string)
    
    Optional inputs:
    :savefig:      Save and close figure (default is True)
    :saveas:       Name to save figure as (default is <MSID>.png)
    :samefig:      Use current figure (default is False)
    :start:        Start time (default is after OAC on 1999:250)
    :stop:         Stop time (default is None)
    :stat:         Statistic type ('5min' or 'daily', default is 'daily')
    :filter:       User-defined Start and End times to filter out due to bad 
                   data.  If none are supplied, it will default to any listed 
                   in filter_times.py.  In addition, LTTplot will always 
                   filter known NSM and SSM events as listed in 
                   filter_times.py (bad_all).
    :plot_stds:    Plot standard deviations (default is True)
    :plot_mins:    Plot minimum values (default is True)
    :plot_means:   Plot mean values (default is True)
    :plot_maxes:   Plot maximum values (default is True)
    :plot_limits:  Plot database yellow caution and red warning limits 
                   (default is True)
    :yellow:       User-defined yellow caution limit lines (default is none)
    :min_mark:     User-defined marker for minimum values (default is 'b:')
    :max_mark:     User-defined marker for maximum values (default is 'g:')
    :mean_mark:    User-defined marker for mean values (default is 'k+')
    :red:          User-defined red warning limit lines  (default is none)                
    :subplot:      Subplot information in [rows, columns, subplot number] 
                   (default is [1, 1, 1])
    :fig_width:    Figure width (default is 8).  Helpful if x-axis is crowded.
                   Irrelevant if samefig=True.
    :fig_height:   Figure height (default varies by number of subplots:  
                   6 for 1 row of subplots, 9 for 2 rows, otherwise 12).
                   Irrelevant if samefig=True.
    :ylim:         User-defined  y-limits (default is none)
    
    :legend:       Display legend (default is False)
    :cust_title:   Custom title (default is MSID and description)
    :cust_unit:    Custom unit to be displayed on y-axis label, typically for 
                   use with custom_mult or derived parameters (default is 
                   none)
    :custom_mult:  Custom multiplier, typically for use with custom unit 
                   (default is none)   
    
    e.g.
    LTTplot('Dist_SatEarth')
    LTTplot('pline05t', ylim=[30,170], savefig=False) 
    LTTplot('pr1tv01t', limit_lines=False, yellow=150, red=240)
    LTTplot('pr2tv01t', limit_lines=False, yellow=[40,150], red=[37,240])
    LTTplot('plaed3gt', filter=['2011:299:00:00:00 2011:300:00:00:00'])
    LTTplot('pcm01t', subplot=[4,1,1], savefig=False) 
    LTTplot('aogbias1', cust_unit='ARCSEC/SEC', cust_mult=3600*180/pi, 
            subplot=311)
    LTTplot('aosares1', start='2003:001', stop='2003:100', fig_width=10, 
            fig_height=6)
    LTTplot('dp_css1_npm_sun', plot_means=False, plot_maxes=False, 
             plot_stds=False, min_mark='rd', legend=True)
    """
    var = var.lower()
    start = kwargs.pop('start', '1999:250')
    stop = kwargs.pop('stop', None)
    stat = kwargs.pop('stat', 'daily')
    
    # Collect data and filter for bad points
    data = fetch.Msid(var, start, stop, stat=stat)
    data.filter_bad_times(table=getattr(bad, 'bad_all'))
    if kwargs.has_key('filter'):
        data.filter_bad_times(table=kwargs.pop('filter'))
    elif hasattr(bad, 'bad_' + var):
        data.filter_bad_times(table=getattr(bad, 'bad_' + var))
    
    # Define subplots and figure size
    # Figure size will vary depending on the number of subplots. If 
    # plotting standard deviations, ax1 will only be used to reference 
    # default axes size.  ax1 will be deleted and data will be plotted on ax2.
    sub = kwargs.pop('subplot', 111)
    # Convert subplot input to list form if provided by user as integer
    if np.isscalar(sub):
        sub = [int(str(sub)[0]), int(str(sub)[1]), int(str(sub)[2])]
    # Create a new figure unless using existing figure
    if not kwargs.pop('samefig', False):
        if kwargs.has_key('fig_height'):
            fig_height = kwargs.pop('fig_height')
        elif sub[0] == 1:  
            fig_height = 6
        elif sub[0] == 2:  
            fig_height = 6
        else:  
            fig_height = 12
        fig_width = kwargs.pop('fig_width', 8)
        pp.figure(figsize=(fig_width, fig_height))
    ax1 = pp.subplot(sub[0], sub[1], sub[2])
    ax1.ticklabel_format(useOffset=False)
    if kwargs.get('plot_stds', True):
        ax_pos = ax1.get_position().get_points()
        ax_width = ax_pos[1,0] - ax_pos[0,0]
        ax_height = ax_pos[1,1] - ax_pos[0,1]
        pp.delaxes(ax1)
        ax2 = pp.axes([ax_pos[0,0], ax_pos[0,1] + .20 * ax_height, ax_width, 
                      .75 * ax_height])  
        ax2.ticklabel_format(useOffset=False)        
    
    # Plot data
    mult = kwargs.pop('cust_mult', 1)    
    lim = kwargs.pop('limit_lines', True)
    if kwargs.pop('plot_maxes', True):
        plot_cxctime(data.times, data.maxes * mult, 
                     kwargs.pop('max_mark', 'g.'), markersize=3, label=(stat + ' maxes'))
    if kwargs.pop('plot_mins', True):
        plot_cxctime(data.times, data.mins * mult, 
                     kwargs.pop('min_mark', 'b.'), markersize=3, label=(stat + ' mins'))
    if kwargs.pop('plot_means', True):
        plot_cxctime(data.times, data.means * mult, 
                     kwargs.pop('mean_mark', 'k.'), markersize=3, label=(stat + ' means'))
  
    # Adjust x-axis
    x_ax = Time.DateTime(pp.xlim(), format='plotdate').mjd
    dur = np.diff(x_ax)
    x_ax_new = [x_ax[0], x_ax[1] + .1*dur[0]]
    pp.xlim(Time.DateTime(x_ax_new, format='mjd').plotdate)

    # Plot limits
    if kwargs.pop('plot_limits', True):
        # Check if single limit set exists in TDB
        if (hasattr(data, 'tdb') and (data.tdb.Tlmt is not None)):
            pp.plot(pp.xlim(), np.array([data.tdb.Tlmt[4] * mult, 
                                         data.tdb.Tlmt[4] * mult]), 'r')
            pp.plot(pp.xlim(), np.array([data.tdb.Tlmt[2] * mult, 
                                         data.tdb.Tlmt[2] * mult]), 'y')
            pp.plot(pp.xlim(), np.array([data.tdb.Tlmt[3] * mult, 
                                         data.tdb.Tlmt[3] * mult]), 'y')
            pp.plot(pp.xlim(), np.array([data.tdb.Tlmt[5] * mult, 
                                         data.tdb.Tlmt[5] * mult]), 'r')  
            if ~kwargs.has_key('ylim'):
                pp.ylim(np.array([data.tdb.Tlmt[4] - 10.0, 
                                  data.tdb.Tlmt[5] + 10.0]))
        
    # Add title
    if kwargs.has_key('cust_title'):
        title = kwargs.pop('cust_title')
    elif hasattr(data, 'tdb'):
        title = data.tdb.technical_name + ' - ' + data.msid.upper() 
    else:
        title=data.msid.upper()    
    pp.title(title)
    
    # Account for custom y-labels
    if kwargs.has_key('cust_unit'):
        pp.ylabel(kwargs.pop('cust_unit'))
    else:
        pp.ylabel(data.unit)
    
    pp.grid()
    
    # Plot custom limit lines
    if kwargs.has_key('ylim'):
        pp.ylim(kwargs.pop('ylim'))
    if kwargs.has_key('yellow'):
        y = np.array([kwargs.pop('yellow')])
        for i in range(len(y)):
            pp.plot(pp.xlim(), np.array([y[i], y[i]]), 'y') 
    if kwargs.has_key('red'):
        r = np.array([kwargs.pop('red')])
        for i in range(len(r)):
            pp.plot(pp.xlim(), np.array([r[i], r[i]]), 'r')        
    
    # Add legend
    if kwargs.pop('legend', False):
        pp.legend(loc='best')
    
    # Plot standard deviations on ax3
    if kwargs.get('plot_stds', True):
        ax2.set_xticklabels([])
        ax3 = pp.axes([ax_pos[0,0], ax_pos[0,1] + .05 * ax_height, 
                       ax_width, .15 * ax_height])
        plot_cxctime(data.times, data.stds * mult, color='k', 
                     label=(stat + ' stdev'))
        ax3.yaxis.set_major_locator(ticker.MaxNLocator(2))
        y_ticks = pp.yticks()
        y_lim = pp.ylim()
        pp.xlim(Time.DateTime(x_ax_new, format='mjd').plotdate) 
        # prevent overlap between y-axis and stdev y-axis
        if (y_lim[1] - y_ticks[0][-1]) / y_lim[-1] < .70:
            pp.yticks(y_ticks[0][:-1])
        
       
    # Ensure xticks aren't rotated
    ax = pp.gca()
    pp.setp(ax.get_xticklabels(), 'rotation', 0)
    
    # Save and close figure
    s = kwargs.pop('savefig', True)
    if s == True:
        figname = kwargs.pop('saveas', data.msid.lower() + '.png')
        pp.savefig(figname)
        pp.close()


##-------------------------------------------------------------
# Define PCAD Custom LTT Plots

def pcad_ltts(start, stop):

    # ACA --------------------------------------------
    #
    plot_ltt('aacccdpt', start=start, stop=stop, **pcad.plot_aacccdpt)
    plot_ltt('aflcaah', start=start, stop=stop, **pcad.plot_aflcaah)

    # Min CSS Counts in NPM, Sun ---------------------
    plot_ltt('dp_css1_npm_sun', start=start, stop=stop, 
             **pcad.plot_dp_css1_npm_sun)
    plot_ltt('dp_css2_npm_sun', start=start, stop=stop, 
             **pcad.plot_dp_css2_npm_sun)
    plot_ltt('dp_css3_npm_sun', start=start, stop=stop, 
             **pcad.plot_dp_css3_npm_sun)
    plot_ltt('dp_css4_npm_sun', start=start, stop=stop, 
             **pcad.plot_dp_css4_npm_sun)  
    
    # FSS Angles -------------------------------------
    #
    plot_ltt('dp_roll_fss', start=start, stop=stop, **pcad.plot_dp_roll_fss)          
    plot_ltt('dp_pitch_fss', start=start, stop=stop, **pcad.plot_dp_pitch_fss)        
    #
    plot_ltt('aoalpang', start=start, stop=stop, **pcad.plot_aoalpang)                
    plot_ltt('aobetang', start=start, stop=stop, **pcad.plot_aobetang)                

    # FSS / CSS Sun Vector Difference ----------------
    plot_ltt('dp_fss_css_angle_diff', start=start, stop=stop, 
             **pcad.plot_dp_fss_css_angle_diff)            

    # Solar Array Angles -----------------------------
    #
    plot_ltt('aosares1', start=start, stop=stop, **pcad.plot_aosares1)               
    plot_ltt('aosares2', start=start, stop=stop, **pcad.plot_aosares2)               
    
    # IRU-1 ------------------------------------------
    if Time.DateTime(start).secs < Time.DateTime('2003:200').secs:
        if Time.DateTime(stop).secs > Time.DateTime('2003:200').secs:
            stop_iru1 = '2003:199'
        else:  
            stop_iru1 = stop
        #
        plot_ltt('airu1g1i', start=start, stop=stop_iru1, **pcad.plot_airu1g1i)              
        plot_ltt('airu1g2i', start=start, stop=stop_iru1, **pcad.plot_airu1g2i)              
        #
        plot_ltt('airu1g1t', start=start, stop=stop_iru1, **pcad.plot_airu1g1t)              
        plot_ltt('airu1g2t', start=start, stop=stop_iru1, **pcad.plot_airu1g2t)              
        #
        plot_ltt('airu1bt', start=start, stop=stop_iru1, **pcad.plot_airu1bt)                
        plot_ltt('airu1vft', start=start, stop=stop_iru1, **pcad.plot_airu1vft)              

    # IRU-2 ------------------------------------------
    if Time.DateTime(stop).secs > Time.DateTime('2003:201').secs:
        if Time.DateTime(start).secs < Time.DateTime('2003:201').secs:
            start_iru2 = '2003:201'
        else:  
            start_iru2 = start
        #
        plot_ltt('airu2g1i', start=start_iru2, stop=stop, **pcad.plot_airu2g1i)              
        plot_ltt('airu2g2i', start=start_iru2, stop=stop, **pcad.plot_airu2g2i)              
        #
        plot_ltt('airu2g1t', start=start_iru2, stop=stop, **pcad.plot_airu2g1t)              
        plot_ltt('airu2g2t', start=start_iru2, stop=stop, **pcad.plot_airu2g2t)              
        #
        plot_ltt('airu2bt', start=start_iru2, stop=stop, **pcad.plot_airu2bt)                
        plot_ltt('airu2vft', start=start_iru2, stop=stop, **pcad.plot_airu2vft)              

    # IRU Biases -------------------------------------
    #
    plot_ltt('aogbias1', start=start, stop=stop, **pcad.plot_aogbias1)                
    plot_ltt('aogbias2', start=start, stop=stop, **pcad.plot_aogbias2)                
    plot_ltt('aogbias3', start=start, stop=stop, **pcad.plot_aogbias3)                

    # RW Speeds --------------------------------------
    #
    plot_ltt('aorwspd1', start=start, stop=stop, **pcad.plot_aorwspd1)                
    plot_ltt('aorwspd2', start=start, stop=stop, **pcad.plot_aorwspd2)                
    plot_ltt('aorwspd3', start=start, stop=stop, **pcad.plot_aorwspd3)                
    #
    plot_ltt('aorwspd4', start=start, stop=stop, **pcad.plot_aorwspd4)                
    plot_ltt('aorwspd5', start=start, stop=stop, **pcad.plot_aorwspd5)                
    plot_ltt('aorwspd6', start=start, stop=stop, **pcad.plot_aorwspd6)                

    # RW Compartment Temperatures ------------------------
    plot_ltt('tcyz_rw1', start=start, stop=stop, **pcad.plot_tcyz_rw1)                
    plot_ltt('tpcp_rw2', start=start, stop=stop, **pcad.plot_tpcp_rw2)                
    plot_ltt('tpcp_rw3', start=start, stop=stop, **pcad.plot_tpcp_rw3)                
    #
    plot_ltt('tpcm_rw4', start=start, stop=stop, **pcad.plot_tpcm_rw4)                
    plot_ltt('tpcm_rw5', start=start, stop=stop, **pcad.plot_tpcm_rw5)                
    plot_ltt('tcyz_rw6', start=start, stop=stop, **pcad.plot_tcyz_rw6)                

    # RW Bearing Temperatures ------------------------
    plot_ltt('arwa1bt', start=start, stop=stop, **pcad.plot_arwa1bt)                 
    plot_ltt('arwa2bt', start=start, stop=stop, **pcad.plot_arwa2bt)                 
    plot_ltt('arwa3bt', start=start, stop=stop, **pcad.plot_arwa3bt)                 
    #
    plot_ltt('arwa4bt', start=start, stop=stop, **pcad.plot_arwa4bt)                 
    plot_ltt('arwa5bt', start=start, stop=stop, **pcad.plot_arwa5bt)                 
    plot_ltt('arwa6bt', start=start, stop=stop, **pcad.plot_arwa6bt)                 

    # RW Delta (Compartment - Bearing) Temperatures ------
    plot_ltt('dp_rw1_delta_temp', start=start, stop=stop, 
             **pcad.plot_dp_rw1_delta_temp)
    plot_ltt('dp_rw2_delta_temp', start=start, stop=stop, 
             **pcad.plot_dp_rw2_delta_temp)
    plot_ltt('dp_rw3_delta_temp', start=start, stop=stop, 
             **pcad.plot_dp_rw3_delta_temp)
    #
    plot_ltt('dp_rw4_delta_temp', start=start, stop=stop, 
             **pcad.plot_dp_rw4_delta_temp)
    plot_ltt('dp_rw5_delta_temp', start=start, stop=stop, 
             **pcad.plot_dp_rw5_delta_temp)
    plot_ltt('dp_rw6_delta_temp', start=start, stop=stop, 
             **pcad.plot_dp_rw6_delta_temp)

    # RW Torque Currents -----------------------------
    #
    plot_ltt('awd1tqi', start=start, stop=stop, **pcad.plot_awd1tqi)                 
    plot_ltt('awd2tqi', start=start, stop=stop, **pcad.plot_awd2tqi)                 
    plot_ltt('awd3tqi', start=start, stop=stop, **pcad.plot_awd3tqi)                 
    #
    plot_ltt('awd4tqi', start=start, stop=stop, **pcad.plot_awd4tqi)                 
    plot_ltt('awd5tqi', start=start, stop=stop, **pcad.plot_awd5tqi)                 
    plot_ltt('awd6tqi', start=start, stop=stop, **pcad.plot_awd6tqi)                 

    # RW Commanded Torque ---------------------------------
    #
    plot_ltt('aorwcmd1', start=start, stop=stop, **pcad.plot_aorwcmd1)               
    plot_ltt('aorwcmd2', start=start, stop=stop, **pcad.plot_aorwcmd2)               
    plot_ltt('aorwcmd3', start=start, stop=stop, **pcad.plot_aorwcmd3)               
    #
    plot_ltt('aorwcmd4', start=start, stop=stop, **pcad.plot_aorwcmd4)               
    plot_ltt('aorwcmd5', start=start, stop=stop, **pcad.plot_aorwcmd5)               
    plot_ltt('aorwcmd6', start=start, stop=stop, **pcad.plot_aorwcmd6)               
       
    # WDE Converter Voltages -------------------------
    #
    plot_ltt('awd1cv5v', start=start, stop=stop, **pcad.plot_awd1cv5v)               
    plot_ltt('awd2cv5v', start=start, stop=stop, **pcad.plot_awd2cv5v)               
    plot_ltt('awd3cv5v', start=start, stop=stop, **pcad.plot_awd3cv5v)               
    #
    plot_ltt('awd4cv5v', start=start, stop=stop, **pcad.plot_awd4cv5v)               
    plot_ltt('awd5cv5v', start=start, stop=stop, **pcad.plot_awd5cv5v)               
    plot_ltt('awd6cv5v', start=start, stop=stop, **pcad.plot_awd6cv5v)               

    # Other Converter Voltages -----------------------
    #
    plot_ltt('acpa5cv', start=start, stop=stop, **pcad.plot_acpa5cv)           
    plot_ltt('ade1p5cv', start=start, stop=stop, **pcad.plot_ade1p5cv)         
    plot_ltt('aspea5cv', start=start, stop=stop, **pcad.plot_aspea5cv)  
    
    plot_ltt('afsspc1v', start=start, stop=stop, **pcad.plot_afsspc1v)         
    plot_ltt('afsspc2v', start=start, stop=stop, **pcad.plot_afsspc2v)         
    
    plot_ltt('agws1v', start=start, stop=stop, **pcad.plot_agws1v)             
    plot_ltt('agws2v', start=start, stop=stop, **pcad.plot_agws2v)             
    plot_ltt('aioap5cv', start=start, stop=stop, **pcad.plot_aioap5cv)         
    
    plot_ltt('avd1cv5v', start=start, stop=stop, **pcad.plot_avd1cv5v) 
    plot_ltt('avd2cv5v', start=start, stop=stop, **pcad.plot_avd2cv5v)     

    # EPIC Register Mismatches & CPE Error Count ------
    #
    plot_ltt('aoepicer', start=start, stop=stop, **pcad.plot_aoepicer)               
    plot_ltt('aocpestc', start=start, stop=stop, **pcad.plot_aocpestc)       
    
    # Pointing Control (Attitude Errors) --------------
    # 
    plot_ltt('aoatter2', start=start, stop=stop, **pcad.plot_aoatter2)
    plot_ltt('aoatter3', start=start, stop=stop, **pcad.plot_aoatter3)    


##-------------------------------------------------------------
# Define PROP Custom LTT Plots
def prop_ltts(start, stop):
    plot_ltt('pcm01t', start=start, stop=stop, **prop.plot_pcm01t)
    plot_ltt('pcm02t', start=start, stop=stop, **prop.plot_pcm02t)
    plot_ltt('pcm03t', start=start, stop=stop, **prop.plot_pcm03t)
    plot_ltt('pcm04t', start=start, stop=stop, **prop.plot_pcm04t)
    plot_ltt('pfdm101t', start=start, stop=stop, **prop.plot_pfdm101t)
    plot_ltt('pfdm102t', start=start, stop=stop, **prop.plot_pfdm102t)
    plot_ltt('pfdm201t', start=start, stop=stop, **prop.plot_pfdm201t)
    plot_ltt('pfdm202t', start=start, stop=stop, **prop.plot_pfdm202t)
    plot_ltt('pffp01t', start=start, stop=stop, **prop.plot_pffp01t)
    plot_ltt('pftank1t', start=start, stop=stop, **prop.plot_pftank1t)
    plot_ltt('pftank2t', start=start, stop=stop, **prop.plot_pftank2t)
    plot_ltt('pftankip', start=start, stop=stop, **prop.plot_pftankip)
    plot_ltt('pftankop', start=start, stop=stop, **prop.plot_pftankop)
    plot_ltt('phetankp', start=start, stop=stop, **prop.plot_phetankp)
    plot_ltt('phetankt', start=start, stop=stop, **prop.plot_phetankt)
    plot_ltt('phofp1t', start=start, stop=stop, **prop.plot_phofp1t)
    plot_ltt('plaed1at', start=start, stop=stop, **prop.plot_plaed1at)
    plot_ltt('plaed1bt', start=start, stop=stop, **prop.plot_plaed1bt)
    plot_ltt('plaed1ct', start=start, stop=stop, **prop.plot_plaed1ct)
    plot_ltt('plaed1dt', start=start, stop=stop, **prop.plot_plaed1dt)
    plot_ltt('plaed1et', start=start, stop=stop, **prop.plot_plaed1et)
    plot_ltt('plaed1ft', start=start, stop=stop, **prop.plot_plaed1ft)
    plot_ltt('plaed1gt', start=start, stop=stop, **prop.plot_plaed1gt)
    plot_ltt('plaed1ht', start=start, stop=stop, **prop.plot_plaed1ht)
    plot_ltt('plaed1it', start=start, stop=stop, **prop.plot_plaed1it)
    plot_ltt('plaed2at', start=start, stop=stop, **prop.plot_plaed2at)
    plot_ltt('plaed2bt', start=start, stop=stop, **prop.plot_plaed2bt)
    plot_ltt('plaed2ct', start=start, stop=stop, **prop.plot_plaed2ct)
    plot_ltt('plaed2dt', start=start, stop=stop, **prop.plot_plaed2dt)
    plot_ltt('plaed2et', start=start, stop=stop, **prop.plot_plaed2et)
    plot_ltt('plaed2ft', start=start, stop=stop, **prop.plot_plaed2ft)
    plot_ltt('plaed2gt', start=start, stop=stop, **prop.plot_plaed2gt)
    plot_ltt('plaed2ht', start=start, stop=stop, **prop.plot_plaed2ht)
    plot_ltt('plaed2it', start=start, stop=stop, **prop.plot_plaed2it)
    plot_ltt('plaed3at', start=start, stop=stop, **prop.plot_plaed3at)
    plot_ltt('plaed3bt', start=start, stop=stop, **prop.plot_plaed3bt)
    plot_ltt('plaed3ct', start=start, stop=stop, **prop.plot_plaed3ct)
    plot_ltt('plaed3dt', start=start, stop=stop, **prop.plot_plaed3dt)
    plot_ltt('plaed3et', start=start, stop=stop, **prop.plot_plaed3et)
    plot_ltt('plaed3ft', start=start, stop=stop, **prop.plot_plaed3ft)
    plot_ltt('plaed3gt', start=start, stop=stop, **prop.plot_plaed3gt)
    plot_ltt('plaed3ht', start=start, stop=stop, **prop.plot_plaed3ht)
    plot_ltt('plaed3it', start=start, stop=stop, **prop.plot_plaed3it)
    plot_ltt('plaed4at', start=start, stop=stop, **prop.plot_plaed4at)
    plot_ltt('plaed4bt', start=start, stop=stop, **prop.plot_plaed4bt)
    plot_ltt('plaed4ct', start=start, stop=stop, **prop.plot_plaed4ct)
    plot_ltt('plaed4dt', start=start, stop=stop, **prop.plot_plaed4dt)
    plot_ltt('plaed4et', start=start, stop=stop, **prop.plot_plaed4et)
    plot_ltt('plaed4ft', start=start, stop=stop, **prop.plot_plaed4ft)
    plot_ltt('plaed4gt', start=start, stop=stop, **prop.plot_plaed4gt)
    plot_ltt('plaed4ht', start=start, stop=stop, **prop.plot_plaed4ht)
    plot_ltt('plaed4it', start=start, stop=stop, **prop.plot_plaed4it)
    plot_ltt('plaev1at', start=start, stop=stop, **prop.plot_plaev1at)
    plot_ltt('plaev1bt', start=start, stop=stop, **prop.plot_plaev1bt)
    plot_ltt('plaev2at', start=start, stop=stop, **prop.plot_plaev2at)
    plot_ltt('plaev2bt', start=start, stop=stop, **prop.plot_plaev2bt)
    plot_ltt('plaev3at', start=start, stop=stop, **prop.plot_plaev3at)
    plot_ltt('plaev3bt', start=start, stop=stop, **prop.plot_plaev3bt)
    plot_ltt('plaev4at', start=start, stop=stop, **prop.plot_plaev4at)
    plot_ltt('plaev4bt', start=start, stop=stop, **prop.plot_plaev4bt)
    plot_ltt('pline01t', start=start, stop=stop, **prop.plot_pline01t)
    plot_ltt('pline02t', start=start, stop=stop, **prop.plot_pline02t)
    plot_ltt('pline03t', start=start, stop=stop, **prop.plot_pline03t)
    plot_ltt('pline04t', start=start, stop=stop, **prop.plot_pline04t)
    plot_ltt('pline05t', start=start, stop=stop, **prop.plot_pline05t)
    plot_ltt('pline06t', start=start, stop=stop, **prop.plot_pline06t)
    plot_ltt('pline07t', start=start, stop=stop, **prop.plot_pline07t)
    plot_ltt('pline08t', start=start, stop=stop, **prop.plot_pline08t)
    plot_ltt('pline09t', start=start, stop=stop, **prop.plot_pline09t)
    plot_ltt('pline10t', start=start, stop=stop, **prop.plot_pline10t)
    plot_ltt('pline11t', start=start, stop=stop, **prop.plot_pline11t)
    plot_ltt('pline12t', start=start, stop=stop, **prop.plot_pline12t)
    plot_ltt('pline13t', start=start, stop=stop, **prop.plot_pline13t)
    plot_ltt('pline14t', start=start, stop=stop, **prop.plot_pline14t)
    plot_ltt('pline15t', start=start, stop=stop, **prop.plot_pline15t)
    plot_ltt('pline16t', start=start, stop=stop, **prop.plot_pline16t)
    plot_ltt('pm1thv1t', start=start, stop=stop, **prop.plot_pm1thv1t)
    plot_ltt('pm1thv2t', start=start, stop=stop, **prop.plot_pm1thv2t)
    plot_ltt('pm2thv1t', start=start, stop=stop, **prop.plot_pm2thv1t)
    plot_ltt('pm2thv2t', start=start, stop=stop, **prop.plot_pm2thv2t)
    plot_ltt('pm3thv1t', start=start, stop=stop, **prop.plot_pm3thv1t)
    plot_ltt('pm3thv2t', start=start, stop=stop, **prop.plot_pm3thv2t)
    plot_ltt('pm4thv1t', start=start, stop=stop, **prop.plot_pm4thv1t)
    plot_ltt('pm4thv2t', start=start, stop=stop, **prop.plot_pm4thv2t)
    plot_ltt('pmfp01t', start=start, stop=stop, **prop.plot_pmfp01t)
    plot_ltt('pmtank1t', start=start, stop=stop, **prop.plot_pmtank1t)
    plot_ltt('pmtank2t', start=start, stop=stop, **prop.plot_pmtank2t)
    plot_ltt('pmtank3t', start=start, stop=stop, **prop.plot_pmtank3t)
    plot_ltt('pmtankp', start=start, stop=stop, **prop.plot_pmtankp)
    plot_ltt('pr1tv01t', start=start, stop=stop, **prop.plot_pr1tv01t)
    plot_ltt('pr1tv02t', start=start, stop=stop, **prop.plot_pr1tv02t)
    plot_ltt('pr2tv01t', start=start, stop=stop, **prop.plot_pr2tv01t)
    plot_ltt('pr2tv02t', start=start, stop=stop, **prop.plot_pr2tv02t)
    plot_ltt('pr3tv01t', start=start, stop=stop, **prop.plot_pr3tv01t)
    plot_ltt('pr3tv02t', start=start, stop=stop, **prop.plot_pr3tv02t)
    plot_ltt('pr4tv01t', start=start, stop=stop, **prop.plot_pr4tv01t)
    plot_ltt('pr4tv02t', start=start, stop=stop, **prop.plot_pr4tv02t)
    plot_ltt('pxdm01t', start=start, stop=stop, **prop.plot_pxdm01t)
    plot_ltt('pxdm02t', start=start, stop=stop, **prop.plot_pxdm02t)
    plot_ltt('pxtank1t', start=start, stop=stop, **prop.plot_pxtank1t)
    plot_ltt('pxtank2t', start=start, stop=stop, **prop.plot_pxtank2t)
    plot_ltt('pxtankip', start=start, stop=stop, **prop.plot_pxtankip)
    plot_ltt('pxtankop', start=start, stop=stop, **prop.plot_pxtankop)

##-------------------------------------------------------------
# Define PROP Custom LTT Plots
def prop_zoom_ltts(start, stop):
    plot_ltt('pcm01t', ylim=[95,150], plot_limits=False, yellow=[85,145], 
            red=[80,160])
    plot_ltt('pcm02t', ylim=[95,150], plot_limits=False, yellow=[85,145], 
            red=[80,160])
    plot_ltt('pcm03t', ylim=[95,150], plot_limits=False, yellow=[65,145], 
            red=[60,160])
    plot_ltt('pcm04t', ylim=[95,150], plot_limits=False, yellow=[65,145], 
            red=[60,160])
    plot_ltt('pmtank1t', ylim=[65,105])
    plot_ltt('pmtank2t', ylim=[65,105])
    plot_ltt('pmtank3t', ylim=[65,105])
    plot_ltt('pftank1t', ylim=[65,105], plot_limits=False, yellow=[47,100], 
            red=[40,120])
    plot_ltt('pftank2t', ylim=[65,105], plot_limits=False, yellow=[47,100], 
            red=[40,120])
    plot_ltt('pftankip', ylim=[275, 305])
    plot_ltt('pftankop', ylim=[275, 305])

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    