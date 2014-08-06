import os
import numpy
from sklearn.metrics import mean_squared_error
from math import sqrt
import tools
from pyRMSD.condensedMatrix import CondensedMatrix
from pyproct.driver.handlers.matrix.matrixHandler import MatrixHandler
import copy
from pyproct.clustering.clustering import Clustering
import sklearn.metrics
import math

campari_RDCs = numpy.load(os.path.join("RDCvsRMSD","q_fit_campari.npy"))
profasi_RDCs = numpy.load(os.path.join("RDCvsRMSD","q_fit_profasi.npy"))

tools.create_dir(os.path.join("RDCvsRMSD","campari","RMSD"))
tools.create_dir(os.path.join("RDCvsRMSD","campari","RDC"))

PYPROCT = "/home/victor/workspaces/Python/pyProClust/pyproct/main.py"

# number_of_models = len(campari_RDCs)
# ## Create RDC matrix
# matrix_data = []
# for i in range(0, number_of_models-1):
#     for j in range(i+1, number_of_models):
#         matrix_data.append(sqrt(mean_squared_error(campari_RDCs[i], campari_RDCs[j])))
#
# handler = MatrixHandler( { "method": "load" })
# handler.distance_matrix = CondensedMatrix(matrix_data)
# handler.save_matrix(os.path.join("RDCvsRMSD", "campari", "RDC", "matrix"))

# template_script = {
#     "clustering": {
#         "generation": {
#             "method": "generate"
#         },
#         "evaluation": {
#             "maximum_noise": 15,
#             "evaluation_criteria": {
#                 "criteria_0": {
#                     "CythonSilhouette": {
#                         "action": ">",
#                         "weight": 3
#                     },
#                     "CythonMirrorCohesion": {
#                         "action": ">",
#                         "weight": 2
#                     }
#                 }
#             },
#             "minimum_cluster_size": 50,
#             "query_types": [
#                 "NumClusters",
#                 "NoiseLevel",
#                 "MeanClusterSize"
#             ],
#             "maximum_clusters": 200,
#             "minimum_clusters": 6
#         },
#         "algorithms": {
#             "kmedoids": {
#                 "max": 50,
#                 "seeding_type": "RANDOM",
#                 "tries": 5
#             },
#             "hierarchical": {
#             },
#             "dbscan": {
#                 "max": 50
#             },
#             "gromos": {
#                 "max": 50
#             }
#         }
#     },
#     "global": {
#         "control": {
#             "number_of_processes": 7,
#             "scheduler_type": "Process/Parallel"
#         },
#         "workspace": {
#             "base": ""
#         }
#     },
#     "data": {
#         "files": [
#         ],
#         "type": "pdb_ensemble",
#         "matrix": {
#             "method": "rmsd",
#             "parameters": {
#                 "calculator_type": "QCP_OMP_CALCULATOR",
#                 "fit_selection": "backbone"
#             },
#             "image":{
#                 "filename":"matrix_plot"
#             }
#         }
#     },
#     "postprocess": {
#         "representatives":{}
#     }
# }
#
#
# RMSD_script = copy.deepcopy(template_script)
# RMSD_script["global"]["workspace"]["base"] = os.path.join("RDCvsRMSD", "campari", "RMSD", "clustering")
# RMSD_script["data"]["files"].append(os.path.join("RDCvsRMSD", "campari.pdb"))
#
# RCD_script = copy.deepcopy(template_script)
# RCD_script["global"]["workspace"]["base"] = os.path.join("RDCvsRMSD", "campari", "RDC", "clustering")
# RCD_script["data"]["matrix"]["method"] = "load"
# RCD_script["data"]["matrix"]["parameters"]["path"] = os.path.join("RDCvsRMSD", "campari", "RDC", "matrix")
# RCD_script["data"]["files"].append(os.path.join("RDCvsRMSD", "campari.pdb"))
#
# tools.save_dic_in_json(RCD_script, os.path.join("RDCvsRMSD", "campari", "RDC", "script.json"))
# tools.save_dic_in_json(RMSD_script, os.path.join("RDCvsRMSD", "campari", "RMSD", "script.json"))
#
# os.system("python %s %s "%(PYPROCT, os.path.join("RDCvsRMSD", "campari", "RDC", "script.json")))
# os.system("python %s %s "%(PYPROCT, os.path.join("RDCvsRMSD", "campari", "RMSD", "script.json")))


results = tools.load_dic_in_json(os.path.join("RDCvsRMSD", "campari", "RDC_refined", "clustering","results","results.json"))
RDC_clustering = Clustering.from_dic(results["selected"][results["best_clustering"]]["clustering"]).gen_class_list(number_of_elements = 5926)

results = tools.load_dic_in_json(os.path.join("RDCvsRMSD", "campari", "RMSD_refined", "clustering","results","results.json"))
RMSD_clustering = Clustering.from_dic(results["selected"][results["best_clustering"]]["clustering"]).gen_class_list(number_of_elements = 5926)

results = tools.load_dic_in_json(os.path.join("RDCvsRMSD", "campari", "Dihedral", "clustering","results","results.json"))
Dihedral_clustering = Clustering.from_dic(results["selected"][results["best_clustering"]]["clustering"]).gen_class_list(number_of_elements = 5926)

results = tools.load_dic_in_json(os.path.join("RDCvsRMSD", "campari", "Dihedral", "clustering","results","results.json"))
Dihedral_bad_score = Clustering.from_dic(results["selected"]["clustering_0098"]["clustering"]).gen_class_list(number_of_elements = 5926)

results = tools.load_dic_in_json(os.path.join("RDCvsRMSD", "campari", "Dihedral", "clustering","results","results.json"))
Dihedral_medium_score = Clustering.from_dic(results["selected"]["clustering_0056"]["clustering"]).gen_class_list(number_of_elements = 5926)

results = tools.load_dic_in_json(os.path.join("RDCvsRMSD", "campari", "Dihedral", "clustering","results","results.json"))
Dihedral_fairly_good_score = Clustering.from_dic(results["selected"]["clustering_0212"]["clustering"]).gen_class_list(number_of_elements = 5926)


# print sklearn.metrics.adjusted_rand_score(RDC_clustering,RMSD_clustering), sklearn.metrics.adjusted_mutual_info_score(RDC_clustering,RMSD_clustering)
# print sklearn.metrics.adjusted_rand_score(RMSD_clustering,Dihedral_clustering), sklearn.metrics.adjusted_mutual_info_score(RMSD_clustering,Dihedral_clustering)
print sklearn.metrics.adjusted_rand_score(RDC_clustering,Dihedral_clustering), sklearn.metrics.adjusted_mutual_info_score(RDC_clustering,Dihedral_clustering)
# print sklearn.metrics.adjusted_rand_score(Dihedral_clustering,Dihedral_bad_score), sklearn.metrics.adjusted_mutual_info_score(Dihedral_clustering,Dihedral_bad_score)
# print sklearn.metrics.adjusted_rand_score(Dihedral_clustering,Dihedral_medium_score), sklearn.metrics.adjusted_mutual_info_score(Dihedral_clustering,Dihedral_medium_score)
# print sklearn.metrics.adjusted_rand_score(Dihedral_clustering,Dihedral_fairly_good_score), sklearn.metrics.adjusted_mutual_info_score(Dihedral_clustering,Dihedral_medium_score)
# print sklearn.metrics.adjusted_rand_score(Dihedral_clustering,Dihedral_clustering), sklearn.metrics.adjusted_mutual_info_score(Dihedral_clustering,Dihedral_clustering)




# Profasi


def rmsd(a,b):
    return math.sqrt(((a-b)**2).sum()/len(a))

number_of_models = len(profasi_RDCs)
print campari_RDCs.shape
print profasi_RDCs.shape

# ## Create RDC matrix
# matrix_data = []
# for i in range(0, number_of_models-1):
#     for j in range(i+1, number_of_models):
#         matrix_data.append(rmsd(profasi_RDCs[i], profasi_RDCs[j]))
#
# handler = MatrixHandler( { "method": "load" })
# handler.distance_matrix = CondensedMatrix(matrix_data)
# handler.save_matrix(os.path.join("RDCvsRMSD", "Profasi", "RDC", "matrix"))

results = tools.load_dic_in_json(os.path.join("RDCvsRMSD", "Profasi", "RDC_refined", "clustering","results","results.json"))
RDC_clustering_pro = Clustering.from_dic(results["selected"][results["best_clustering"]]["clustering"]).gen_class_list(number_of_elements = 7792)

results = tools.load_dic_in_json(os.path.join("RDCvsRMSD", "Profasi", "Dihedral", "clustering","results","results.json"))
Dihedral_clustering_pro = Clustering.from_dic(results["selected"][results["best_clustering"]]["clustering"]).gen_class_list(number_of_elements = 7792)


print sklearn.metrics.adjusted_rand_score(RDC_clustering_pro,Dihedral_clustering_pro), sklearn.metrics.adjusted_mutual_info_score(RDC_clustering,Dihedral_clustering)



print "Done"

