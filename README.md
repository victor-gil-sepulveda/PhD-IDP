PhD-IDP
=======

Scripts to work in the intrinsically disordered proteins project.
Note that this scripts are intended for personal usage and some paths are relative to my own machine.

First tracked in pyProCT' master branch.

Contains 3 scripts:

- fixCampari - Generates a trajectory pdb file from all the single pdb files of the 16 folders corresponding to each temperature.   
- fixProfasi -  Idem, but in this case it also "fixes" each of the single frames by adding the missing MODEL/ENDMDL tags.  
- performComparisons - Generates a conformational sampling comparison script for each of the comparisons we want to perform and executes pyProCT to obtain the result.



