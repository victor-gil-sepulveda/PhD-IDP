'''
Created on 31/03/2014

@author: victor
'''

import os
from pyRMSD.condensedMatrix import CondensedMatrix
from tools import  load_dic_in_json, create_dir, save_dic_in_json
from pyproct.tools.plotTools import matrixToImage


campari_folders = ["N_{:0>3d}".format(i) for i in range(16)]

data = []
for i in range(0,len(campari_folders)-1):
    A_folder = campari_folders[i]
    for j in range(i+1,len(campari_folders)):
        B_folder = campari_folders[j]
        results_file = os.path.join("comparisons","campari", "%s_vs%s_"%(A_folder, B_folder), "results", "conf_space_comp.json")
        print results_file
        if os.path.exists(results_file):
            data.append(load_dic_in_json(results_file)["overlap"])
        else:
            data.append(0.)
print data
matrixToImage(CondensedMatrix(data), "image.png" )
