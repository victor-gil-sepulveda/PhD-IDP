"""
Created on 27/03/2014

@author: victor
"""
import copy
import os

from tools import  load_dic_in_json, create_dir, save_dic_in_json

script_template = load_dic_in_json("template.json")

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

PYPROCT = "/home/victor/workspaces/Python/pyProClust/pyproct/main.py"

initial_i_offset,initial_j_offset = 9, (13-9) # To start aborted runs

# # Campari
# for i in range(initial_i_offset,len(campari_trajs)-1):
#     A_traj = campari_trajs[i]
#     path, file = os.path.split(A_traj)
#     A_traj_id = file.split(".")[0]
#     for j in range(i+1+initial_j_offset,len(campari_trajs)):
#         B_traj = campari_trajs[j]
#         path, file = os.path.split(B_traj)
#         B_traj_id = file.split(".")[0]
#         script = copy.deepcopy(script_template)
#         working_dir = os.path.join("comparisons","campari","%svs%s"%(A_traj_id,B_traj_id))
#         create_dir(working_dir)
#         script["global"]["workspace"]["base"] = working_dir
#         script["data"]["files"] = [A_traj, B_traj]
#         script_path = os.path.join(working_dir,"script.json")
#         save_dic_in_json(script, script_path)
#         os.system("python %s %s "%(PYPROCT, script_path))
#         initial_j_offset = 0
#     initial_i_offset = 0
#
# # Profasi (copy-paste!)
# initial_i_offset,initial_j_offset = 0, 0
# for i in range(initial_i_offset,len(profasi_trajs)-1):
#     A_traj = profasi_trajs[i]
#     path, file = os.path.split(A_traj)
#     A_traj_id = file.split(".")[0]
#     for j in range(i+1+initial_j_offset,len(profasi_trajs)):
#         B_traj = profasi_trajs[j]
#         path, file = os.path.split(B_traj)
#         B_traj_id = file.split(".")[0]
#         script = copy.deepcopy(script_template)
#         working_dir = os.path.join("comparisons","profasi","%svs%s"%(A_traj_id,B_traj_id))
#         create_dir(working_dir)
#         script["global"]["workspace"]["base"] = working_dir
#         script["data"]["files"] = [A_traj, B_traj]
#         script_path = os.path.join(working_dir,"script.json")
#         save_dic_in_json(script, script_path)
#         os.system("python %s %s "%(PYPROCT, script_path))
#         initial_j_offset = 0
#     initial_i_offset = 0

# Campari vs Profasi
for i in [15]: #range(0,len(profasi_trajs)):
    A_traj = campari_trajs[i]
    path, file = os.path.split(A_traj)
    A_traj_id = file.split(".")[0]

    B_traj = profasi_trajs[i]
    path, file = os.path.split(B_traj)
    B_traj_id = file.split(".")[0]

    script = copy.deepcopy(script_template)
    working_dir = os.path.join("comparisons","campari_vs_profasi","%svs%s"%(A_traj_id,B_traj_id))
    create_dir(working_dir)
    script["global"]["workspace"]["base"] = working_dir
    script["data"]["files"] = [{"file":A_traj,"base_selection":"resnum 3to53"},{"file": B_traj,"base_selection":"resnum 3to53"}]
    script_path = os.path.join(working_dir,"script.json")
    save_dic_in_json(script, script_path)
    os.system("python %s %s "%(PYPROCT, script_path))


