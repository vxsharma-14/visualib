# coding: utf-8
def readplotsettings(pfilename):
    '''Function to read input for the plots'''
    import numpy as np
    
    print('Reading plot settings.')
    plot_inputs=np.loadtxt("plotdetails.txt", dtype='str', delimiter=';', skiprows=2)
    filenames = plot_inputs[0,1:5]
    figtitles = plot_inputs[1,1:5]
    xtitles = plot_inputs[2,1:5]
    ytitles = plot_inputs[3,1:5]
    xcoord = plot_inputs[4,1:5]
    ycoord = plot_inputs[5,1:5]
    xcoord = xcoord.astype('float64')
    ycoord = ycoord.astype('float64')
    
    return (filenames, figtitles, xtitles, ytitles, xcoord, ycoord)
