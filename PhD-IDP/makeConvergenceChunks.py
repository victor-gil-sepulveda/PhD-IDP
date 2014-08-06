"""
Created on 22/04/2014

@author: victor
"""
import os
from tools import create_dir, save_dic_in_json
import copy

PYPROCT = "/home/victor/workspaces/Python/pyProClust/pyproct/main.py"

campari_trajs = [
                 {"path":"trajectories/campari/N_000_.pdb", "min":3, "max":15, "noise":5},
                 {"path":"trajectories/campari/N_001_.pdb", "min":5, "max":18, "noise":6},
                 {"path":"trajectories/campari/N_002_.pdb", "min":7, "max":21, "noise":7},
                 {"path":"trajectories/campari/N_003_.pdb", "min":9, "max":24, "noise":8},
                 {"path":"trajectories/campari/N_004_.pdb", "min":11, "max":27, "noise":9},
                 {"path":"trajectories/campari/N_005_.pdb", "min":13, "max":30, "noise":10},
                 {"path":"trajectories/campari/N_006_.pdb", "min":15, "max":33, "noise":11},
                 {"path":"trajectories/campari/N_007_.pdb", "min":17, "max":36, "noise":12},
                 {"path":"trajectories/campari/N_008_.pdb", "min":19, "max":39, "noise":13},
                 {"path":"trajectories/campari/N_009_.pdb", "min":21, "max":42, "noise":15},
                 {"path":"trajectories/campari/N_010_.pdb", "min":23, "max":45, "noise":16},
                 {"path":"trajectories/campari/N_011_.pdb", "min":25, "max":48, "noise":17},
                 {"path":"trajectories/campari/N_012_.pdb", "min":27, "max":51, "noise":18},
                 {"path":"trajectories/campari/N_013_.pdb", "min":29, "max":54, "noise":19},
                 {"path":"trajectories/campari/N_014_.pdb", "min":31, "max":57, "noise":20},
                 {"path":"trajectories/campari/N_015_.pdb", "min":33, "max":60, "noise":21}
                 ]

# profasi_trajs = {
#                  {"path":"trajectories/profasi/t00_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t01_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t02_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t03_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t04_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t05_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t06_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t07_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t08_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t09_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t10_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t11_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t12_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t13_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t14_fixed.pdb", "min":, "max":, "noise":},
#                  {"path":"trajectories/profasi/t15_fixed.pdb", "min":, "max":, "noise":}
#                  }

script_template = {
    "clustering": {
        "generation": {
            "method": "generate"
        },
        "evaluation": {
            "maximum_noise": 15,
            "evaluation_criteria": {
                "criteria_0": {
                    "CythonSilhouette": {
                        "action": ">",
                        "weight": 2
                    },
                    "CythonMirrorCohesion": {
                        "action": ">",
                        "weight": 1
                    }
                }
            },
            "minimum_cluster_size": 15,
            "query_types": [
                "NumClusters",
                "NoiseLevel",
                "MeanClusterSize"
            ],
            "maximum_clusters": 200,
            "minimum_clusters": 30
        },
        "algorithms": {
            "kmedoids": {
                "max": 50,
                "seeding_type": "RANDOM",
                "tries": 3
            },
            "hierarchical": {},
            "dbscan": {},
            "gromos": {
                "max": 50
            }
        }
    },
    "global": {
        "control": {
            "number_of_processes": 7,
            "scheduler_type": "Process/Parallel"
        },
        "workspace": {
            "base": ""
        }
    },
    "data": {
        "files": [
        ],
        "type": "pdb_ensemble",
        "matrix": {
            "method": "rmsd",
            "parameters": {
                "calculator_type": "QCP_OMP_CALCULATOR",
                "fit_selection": "backbone"
            },
#             "image":{
#                 "filename":"matrix_plot"
#             }
        }
    },
    "postprocess": {
       # "representatives":{}
    }
}

def extract_first_n_frames(n, in_trajectory, out_trajectory):
    traj_handler = open(in_trajectory)
    out_traj_handler= open(out_trajectory,"w")

    num_models = 0
    for line in traj_handler:
        out_traj_handler.write(line)

        if line[0:6] == "ENDMDL":
            num_models = num_models+1

        if num_models == n:
            break
    traj_handler.close()
    out_traj_handler.close()

def do_convergence_test(trajectory, traj_type):
    path, file_name = os.path.split(trajectory["path"])
    traj_id = file_name.split(".")[0]
    base_path = os.path.join("convergence",traj_type,"%s"%traj_id)

    for n in range(1000,10000,1000):
        print "- Working with %s with %d frames"%(trajectory["path"],n)
        this_path = os.path.join(base_path, "%d"%n)
        create_dir(this_path)
        pdb_path = os.path.join(this_path,"%d.pdb"%n)
        extract_first_n_frames(n, trajectory["path"], pdb_path)
        script = copy.deepcopy(script_template)
        script["global"]["workspace"]["base"] = this_path
        script["data"]["files"] = [pdb_path]
#         script["clustering"]["evaluation"]["maximum_noise"] = trajectory["noise"]
#         script["clustering"]["evaluation"]["minimum_cluster_size"] = int(n/trajectory["max"])
#         script["clustering"]["evaluation"]["minimum_clusters"] = trajectory["min"]
#         script["clustering"]["evaluation"]["maximum_clusters"] = trajectory["max"]
        script_path = os.path.join(this_path,"script.json")
        save_dic_in_json(script, script_path)
        os.system("python %s %s "%(PYPROCT, script_path))
        os.system("rm %s"%pdb_path)

for traj in campari_trajs:
    do_convergence_test(traj,"campari")

# for traj in profasi_trajs:
#     do_convergence_test(traj, "profasi")




