'''
Created on 23/04/2014

@author: victor
'''
from tools import load_dic_in_json
import os

subfolders = ["1000","2000","3000","4000","5000","6000","7000","8000","9000"]

campari_folders = [
                 "convergence/campari/N_000_",
                 "convergence/campari/N_001_",
                 "convergence/campari/N_002_",
                 "convergence/campari/N_003_",
                 "convergence/campari/N_004_",
                 "convergence/campari/N_005_",
                 "convergence/campari/N_006_",
                 "convergence/campari/N_007_",
                 "convergence/campari/N_008_",
                 "convergence/campari/N_009_",
                 "convergence/campari/N_010_",
                 "convergence/campari/N_011_",
                 "convergence/campari/N_012_",
                 "convergence/campari/N_013_",
                 "convergence/campari/N_014_",
                 "convergence/campari/N_015_"
                 ]

profasi_folders = [
                 "convergence/profasi/t00_fixed",
                 "convergence/profasi/t01_fixed",
                 "convergence/profasi/t02_fixed",
                 "convergence/profasi/t03_fixed",
                 "convergence/profasi/t04_fixed",
                 "convergence/profasi/t05_fixed",
                 "convergence/profasi/t06_fixed",
                 "convergence/profasi/t07_fixed",
                 "convergence/profasi/t08_fixed",
                 "convergence/profasi/t09_fixed",
                 "convergence/profasi/t10_fixed",
                 "convergence/profasi/t11_fixed",
                 "convergence/profasi/t12_fixed",
                 "convergence/profasi/t13_fixed",
                 "convergence/profasi/t14_fixed",
                 "convergence/profasi/t15_fixed"
                 ]
def process_folders(this_folders):
    for folder in this_folders:
        for subfolder in subfolders:
            results_file = os.path.join(folder, subfolder, "results", "results.json")
            if os.path.exists(results_file):
                results = load_dic_in_json(results_file)
                print results_file, results["selected"][results["best_clustering"]]["clustering"]["number_of_clusters"]

process_folders(campari_folders)
