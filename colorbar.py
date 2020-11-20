# coding: utf-8
def cbar_axismap(mappable, ctitle='set title here'):
    '''Function to control the size of colorbar (aspect ratio) in the 
       figure with 2 or 4 subplots.'''
    from mpl_toolkits.axes_grid import make_axes_locatable
    import matplotlib.pyplot as plt
    
    last_axes = plt.gca()
    ax = mappable.axes
    fig = ax.figure
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    cbar = fig.colorbar(mappable, cax=cax, format='%.00')
    cbar.set_label(ctitle, rotation=270, size=12, labelpad=15)
    plt.sca(last_axes)
    
    return cbar
