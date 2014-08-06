"""
Created on 31/03/2014

@author: victor
"""

import os
from pyRMSD.condensedMatrix import CondensedMatrix
from tools import  load_dic_in_json
from pyproct.tools.plotTools import matrixToImage
import matplotlib.pyplot as plt


def process_matrix(folders, image_path, sim_type):
    data = []
    for i in range(0,len(folders)-1):
        A_folder = folders[i]
        for j in range(i+1,len(campari_folders)):
            B_folder = folders[j]
            results_file = os.path.join("comparisons",sim_type, "%svs%s"%(A_folder, B_folder), "results", "conf_space_comp.json")
            print results_file
            if os.path.exists(results_file):
                data.append(load_dic_in_json(results_file)["overlap"])
            else:
                data.append(0.)
    print data
    matrixToImage(CondensedMatrix(data), image_path, diagonal_value=1.)


def process_campari_vs_profasi(campari, profasi):
    data = []
    for i in range(len(campari)):
        A_folder = campari[i]
        B_folder = profasi[i]
        results_file =os.path.join("comparisons","campari_vs_profasi", "%svs%s"%(A_folder, B_folder), "results", "conf_space_comp.json")
        if os.path.exists(results_file):
            data.append(load_dic_in_json(results_file)["overlap"])
        else:
            data.append(0.)
            print results_file, "not found"

    plt.plot(range(len(data)), data, linewidth=2)
    plt.show()


campari_folders = ["N_{:0>3d}_".format(i) for i in range(16)]
profasi_folders = ["t{:0>2d}_fixed".format(i) for i in range(16)]
# process_matrix(campari_folders, "campari_matrix.png", "campari")
# process_matrix(profasi_folders, "profasi_matrix.png", "profasi")
process_campari_vs_profasi(campari_folders, profasi_folders)


