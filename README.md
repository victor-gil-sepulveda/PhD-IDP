PhD-IDP
=======

Scripts to work in the "Intrinsically Disordered Proteins" project.
Note that this scripts are intended for personal usage and some paths are relative to my own machine. In general scripts are run in the PhD-IDP root folder.

First tracked in pyProCT's master branch, then the scripts were moved to their own repo (this one).

This scripts have been used as a whole or with commented parts :D

Contains 4 scripts:

- fixCampari - Generates a trajectory pdb file from all the single pdb files of the 16 folders corresponding to each temperature.   

- fixProfasi -  Idem, but in this case it also "fixes" each of the single frames by adding the missing MODEL/ENDMDL tags.  

- performComparisons - Generates a conformational sampling comparison script for each of the comparisons we want to perform and executes pyProCT to obtain the result.  

- gatherComparisonResults.py - Reads the results of the clusterings generated with the 'perfromComparisons' script and draws the plots.  

- makeConvergenceChunks.py - Prepares chunks of 1000, 2000, 3000 ... elements for each of campari's trajectories and calculates the number of clusters that pyProCT thinks we have there. We expect to see some convergence.  

- gatherConvergenceResults.py - Gathers the number of clusters per temperature, trajectory and trajectory lenght as well as some statistica data about the distance matrices that were calculated.  

- compareRDCsWithRMSD.py - Generates a matrix with RDC distances and then generates two clusterings, one with RDC info and the other with geometrical info. Finally it compares both using the Adjusted Rand Index.

