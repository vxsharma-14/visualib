# coding: utf-8
def create_subplots(nplots, fname, ftitle, xtitle, ytitle, a, b, patch1='False', patch2='False' ):
    '''Function to create a figure with 2 or 4 subplots.'''
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import colorbar as cb
    
    print("Formatting figure fonts.")
    plt.rc('font', family='serif', size=12) # assign fonts and size in the figure
    
    print("Creating figures axes.")
    fig, ax = plt.subplots(figsize=(10,8), dpi=150) # assign size of plot and resolution
    
        
    da = a[1] - a[0]
    db = b[1] - b[0]
    dm = a[3] - a[2]
    dn = b[3] - b[2]
    
    if nplots == 5:
        print("Reading files.")
        x1, y1, p1, x2, y2, p2, x3, y3, p3, x4, y4, p4, im, jm = read4ofiles(fname)
    elif nplots == 3:
        print("Reading files.")
        x1, y1, p1, x2, y2, p2, im, jm = read2ofiles(fname)
    else:
        print('Incorrect values of nplots.')
        print('STOP')
        sys.exit()

    imax = im[0]
    jmax = jm[0]
    xmin = x1[0][0]
    xmax = x1[imax-1][jmax-1]
    ymin = y1[0][0]
    ymax = y1[imax-1][jmax-1]
    
    print('\nGenerating data plot.')
    for i in range (1,nplots):
        if nplots == 5:
            ax = plt.subplot(2,2,i)
        elif nplots == 3:            
            ax = plt.subplot(1,2,i)
        
        if i == 1:
            img1 = plt.pcolormesh(x1, y1, p1, cmap='jet', shading='gouraud')
            cb.cbar_axismap(img1)
            if patch1 == 'True':
                rect1 = patches.Rectangle((a[0], b[0]), da, db, edgecolor='r', facecolor='none')
                ax.add_patch(rect1)
            if patch2 == 'True':
                rect2 = patches.Rectangle((a[2], b[2]), dm, dn, edgecolor='c', facecolor='none')
                ax.add_patch(rect2)

        elif i == 2:
            img2 = plt.pcolormesh(x2, y2, p2, cmap='jet', shading='gouraud')
            cb.cbar_axismap(img2)
            if patch1 == 'True':
                rect1 = patches.Rectangle((a[0], b[0]), da, db, edgecolor='r', facecolor='none')
                ax.add_patch(rect1)
            if patch2 == 'True':
                rect2 = patches.Rectangle((a[2], a[2]), dm, dn, edgecolor='c', facecolor='none')
                ax.add_patch(rect2)
                
        elif nplots == 5 and i == 3:
            img3 = plt.pcolormesh(x3, y3, p3, cmap='jet', shading='gouraud')
            cb.cbar_axismap(img3)
            if patch1 == 'True':
                rect1 = patches.Rectangle((a[0], b[0]), da, db, edgecolor='r', facecolor='none')
                ax.add_patch(rect1)
            if patch2 == 'True':
                rect2 = patches.Rectangle((a[2], b[2]), dm, dn, edgecolor='c', facecolor='none')
                ax.add_patch(rect2)
                
        elif nplots == 5 and i == 4:
            img4 = plt.pcolormesh(x4, y4, p4, cmap='jet', shading='gouraud')
            cb.cbar_axismap(img4)
            if patch1 == 'True':
                rect1 = patches.Rectangle((a[0], b[0]), da, db, edgecolor='r', facecolor='none')
                ax.add_patch(rect1)
            if patch2 == 'True':
                rect2 = patches.Rectangle((a[2], b[2]), dm, dn, edgecolor='c', facecolor='none')
                ax.add_patch(rect2)
                
        plt.xlabel(str(xtitle[i-1]), size=12)
        plt.ylabel(str(ytitle[i-1]), size=12)
        plt.title(str(ftitle[i-1]), size=12)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        #plt.clim(-0.03,0.03)
        plt.tight_layout()
        
        plt.gca().set_aspect('equal', adjustable='box') # set aspect ratio of the plot
    
    plt.show()
    return
def read2ofiles(filename):
    '''Function to read 2 output files for visualization'''
    import numpy as np
    import math
    
    print("Reading plotting data.")
    x1, y1, p1 = np.loadtxt(filename[0], delimiter='\t', unpack=True)
    x2, y2, p2 = np.loadtxt(filename[1], delimiter='\t', unpack=True)
    
    print("Calculating variables.")
    im1 = int(math.sqrt(len(x1)))
    jm1 = int(math.sqrt(len(y1)))
    im2 = int(math.sqrt(len(x2)))
    jm2 = int(math.sqrt(len(y2)))
    
    IM = [im1, im2]
    JM = [jm1, jm2]
    
    print("Organizing data.")
    X1 = np.reshape(x1,(im1,jm1))
    Y1 = np.reshape(y1,(im1,jm1))
    P1 = np.reshape(p1,(im1,jm1))
    X2 = np.reshape(x2,(im2,jm2))
    Y2 = np.reshape(y2,(im2,jm2))
    P2 = np.reshape(p2,(im2,jm2))
    
    return (X1, Y1, P1, X2, Y2, P2, IM, JM)
def read4ofiles(filename):
    '''Function to read 4 output files for visualization'''
    import numpy as np
    import math
    
    print("Reading plotting data.")
    x1, y1, p1 = np.loadtxt(filename[0], delimiter='\t', unpack=True)
    x2, y2, p2 = np.loadtxt(filename[1], delimiter='\t', unpack=True)
    x3, y3, p3 = np.loadtxt(filename[2], delimiter='\t', unpack=True)
    x4, y4, p4 = np.loadtxt(filename[3], delimiter='\t', unpack=True)
    
    print("Calculating variables.")
    im1 = int(math.sqrt(len(x1)))
    jm1 = int(math.sqrt(len(y1)))
    im2 = int(math.sqrt(len(x2)))
    jm2 = int(math.sqrt(len(y2)))
    im3 = int(math.sqrt(len(x3)))
    jm3 = int(math.sqrt(len(y3)))
    im4 = int(math.sqrt(len(x4)))
    jm4 = int(math.sqrt(len(y4)))

    IM = [im1, im2, im3, im4]
    JM = [jm1, jm2, jm3, jm4]
    
    print("Organizing data.")
    X1 = np.reshape(x1,(im1,jm1))
    Y1 = np.reshape(y1,(im1,jm1))
    P1 = np.reshape(p1,(im1,jm1))
    X2 = np.reshape(x2,(im2,jm2))
    Y2 = np.reshape(y2,(im2,jm2))
    P2 = np.reshape(p2,(im2,jm2))
    X3 = np.reshape(x3,(im3,jm3))
    Y3 = np.reshape(y3,(im3,jm3))
    P3 = np.reshape(p3,(im3,jm3))
    X4 = np.reshape(x4,(im4,jm4))
    Y4 = np.reshape(y4,(im4,jm4))
    P4 = np.reshape(p4,(im4,jm4))
    
    return (X1, Y1, P1, X2, Y2, P2, X3, Y3, P3, X4, Y4, P4, IM, JM)
