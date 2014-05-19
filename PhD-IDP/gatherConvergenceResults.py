'''
Created on 23/04/2014

@author: victor
'''
from tools import load_dic_in_json
import os
import matplotlib.pyplot as plt

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

def process_results(this_folders):
    results_matrix = {}
    #fig = plt.figure(figsize=(18, 18))
    # Plot by temperature
    for folder in this_folders:
        subfolder_results = []
        for subfolder in subfolders:
            results_file = os.path.join(folder, subfolder, "results", "results.json")
            if os.path.exists(results_file):
                results = load_dic_in_json(results_file)
                print results_file, results["selected"][results["best_clustering"]]["clustering"]["number_of_clusters"],\
                results["selected"][results["best_clustering"]]["evaluation"]["Noise level"]
                subfolder_results.append(results["selected"][results["best_clustering"]]["clustering"]["number_of_clusters"])
            else:
                subfolder_results.append(0.)
        results_matrix[folder] = subfolder_results
        plt.plot(range(len(subfolders)), subfolder_results, linewidth=2, label = folder.split("/")[2])
    plt.legend(loc=2,prop={'size':6})
    plt.show()

    ## Now plot by trajectory length
    for i in range(len(subfolders)):
        plot_by_size = []
        for folder in this_folders:
            plot_by_size.append(results_matrix[folder][i])
        plt.plot(range(len(this_folders)), plot_by_size, linewidth=2,label = subfolders[i])
    plt.legend(prop={'size':6})
    plt.show()

def process_matrix_stats(this_folders):
    mean = []
    stddev = []
    for folder in this_folders:
        subfolder = "9000"
        matrix_stats_file = os.path.join(folder, subfolder, "matrix", "statistics.json")
        if os.path.exists(matrix_stats_file):
            stats = load_dic_in_json(matrix_stats_file)
            mean.append(stats["Mean"])
            stddev.append(stats["Std. Dev."])
        else:
            mean.append(0)
            stddev.append(0)
        plt.errorbar(range(len(mean)), mean, yerr = stddev, linewidth=2)
    plt.show()

process_results(campari_folders)

process_matrix_stats(campari_folders)

# process_folders(profasi_folders)
