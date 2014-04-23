'''
Created on 22/04/2014

@author: victor
'''
import os
from tools import create_dir, save_dic_in_json
import copy

PYPROCT = "/home/victor/workspaces/Python/pyProClust/pyproct/main.py"

campari_trajs = [
                 "trajectories/campari/N_000_.pdb",
                 "trajectories/campari/N_001_.pdb",
                 "trajectories/campari/N_002_.pdb",
                 "trajectories/campari/N_003_.pdb",
                 "trajectories/campari/N_004_.pdb",
                 "trajectories/campari/N_005_.pdb",
                 "trajectories/campari/N_006_.pdb",
                 "trajectories/campari/N_007_.pdb",
                 "trajectories/campari/N_008_.pdb",
                 "trajectories/campari/N_009_.pdb",
                 "trajectories/campari/N_010_.pdb",
                 "trajectories/campari/N_011_.pdb",
                 "trajectories/campari/N_012_.pdb",
                 "trajectories/campari/N_013_.pdb",
                 "trajectories/campari/N_014_.pdb",
                 "trajectories/campari/N_015_.pdb"
                 ]

profasi_trajs = [
                 "trajectories/profasi/t00_fixed.pdb",
                 "trajectories/profasi/t01_fixed.pdb",
                 "trajectories/profasi/t02_fixed.pdb",
                 "trajectories/profasi/t03_fixed.pdb",
                 "trajectories/profasi/t04_fixed.pdb",
                 "trajectories/profasi/t05_fixed.pdb",
                 "trajectories/profasi/t06_fixed.pdb",
                 "trajectories/profasi/t07_fixed.pdb",
                 "trajectories/profasi/t08_fixed.pdb",
                 "trajectories/profasi/t09_fixed.pdb",
                 "trajectories/profasi/t10_fixed.pdb",
                 "trajectories/profasi/t11_fixed.pdb",
                 "trajectories/profasi/t12_fixed.pdb",
                 "trajectories/profasi/t13_fixed.pdb",
                 "trajectories/profasi/t14_fixed.pdb",
                 "trajectories/profasi/t15_fixed.pdb"
                 ]

script_template = {
    "clustering": {
        "generation": {
            "method": "generate"
        },
        "evaluation": {
            "maximum_noise": 10,
            "evaluation_criteria": {
                "criteria_0": {
                    "CythonSilhouette": {
                        "action": ">",
                        "weight": 3
                    },
                    "CythonMirrorCohesion": {
                        "action": ">",
                        "weight": 2
                    }
                }
            },
            "minimum_cluster_size": 20,
            "query_types": [
                "NumClusters",
                "NoiseLevel",
                "MeanClusterSize"
            ],
            "maximum_clusters": 200,
            "minimum_clusters": 3
        },
        "algorithms": {
            "kmedoids": {
                "max": 25,
                "tries": 5
            },
            "hierarchical": {},
            "dbscan": {},
            "gromos": {
                "max": 25
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
                "fit_selection": "name CA"
            }
        }
    },
    "postprocess": {
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

def do_convergence_test(trajectory):
    path, file_name = os.path.split(trajectory)
    traj_id = file_name.split(".")[0]
    base_path = os.path.join("convergence","campari","%s"%traj_id)
    for n in range(1000,10000,1000):
        print "- Working with %s with %d frames"%(trajectory,n)
        this_path = os.path.join(base_path, "%d"%n)
        create_dir(this_path)
        pdb_path = os.path.join(this_path,"%d.pdb"%n)
        extract_first_n_frames(n, traj, pdb_path)
        script = copy.deepcopy(script_template)
        script["global"]["workspace"]["base"] = this_path
        script["data"]["files"] = [pdb_path]
        script_path = os.path.join(this_path,"script.json")
        save_dic_in_json(script, script_path)
        os.system("python %s %s "%(PYPROCT, script_path))
        os.system("rm %s"%pdb_path)

for traj in campari_trajs:
    do_convergence_test(traj)

for traj in profasi_trajs:
    do_convergence_test(traj)




