# visualib
Functions to visualize and compare 2 or 4 outputs using subplots feature.

Procedure to generate plots from the functions in this reporsitory:

  1. save all files on your machine.
  2. enter details of plots in the file "plotdetails.txt"
     line 3--> name all the output text files maximum 4
     line 4--> enter figure titles maximum 4
     line 5--> X axis title for all the plots maximum 4
     line 6--> Y axis title for all the plots
     line 7--> keep it unchanged (change as required if patch1 = 'True')
     line 8--> keep it unchanged (change as required if patch2 = 'True')
  3. run function readplotsettings(filename argument)** as save the output of the function to 6 objects
  4. run function create_subplots(nplots, fname, ftitle, xtitle, ytitle, a, b, patch1, patch2)**
     nplots = number of sub plots 3 (for 2 subplots) or 5 (for 4 subplots)
     fname = filenames
     ftitle = figure titles
     xtitle = x-axis titles
     ytitle = y-axis titles
     a = x and y coordinates of patch 1 location
     b = x and y coordinates of patch 2 location
     
   **SEE EXAMPLE IN FILE "VISUALIZATION.HTML"
    

