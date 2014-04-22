'''
Created on 22/04/2014

@author: victor
'''
import os
from tools import create_dir

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
    print num_models
    traj_handler.close()
    out_traj_handler.close()

def do_chunks_of_trajs(traj_set):
    for traj in traj_set:
        path, file_name = os.path.split(traj)
        traj_id = file_name.split(".")[0]
        create_dir("chunks/campari/%s"%traj_id)
        for n in range(1000,10000,1000):
            extract_first_n_frames(n, traj, "./chunks/campari/%s/%d.pdb"%(traj_id,n))
            #print n, traj, "chunks/campari/%d.pdb"%n

create_dir("chunks")

create_dir("chunks/campari")
create_dir("chunks/profasi")

do_chunks_of_trajs(campari_trajs)
do_chunks_of_trajs(profasi_trajs)




