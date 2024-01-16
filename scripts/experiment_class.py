import os
import sys
import pandas as pd
from scripts.load_data import load_data
from scripts.processing import single_experiment_processed

# def new_experiments(directory):
#     c = 0
#
#     for file_name, c in directory:
#         channel = c + 1
#         file_name, qcm_dir, note_dir = load_data(directory)
#         filename[channel] = single_experiment_processed.run(file_name, channel)
#
#     return filename[channel]
#
# print(new_experiments("data"))
class Experiment:
    def __init__(self, filename):
    # def __init__(self, filename, channel_number, septin, gtp):
        self.file_name = filename
        # self.channel_number = channel_number
        # self.septin = septin
#     # pass
# print(Experiment)
#
# qcmsept = Experiment('20230718_qcm_sept_slb.csv')
#
# print(file_name)
# c = 0
#
# for files in load_data("data"):
#     c_index += c + 1
#
#     data_c = qcm_dir[channel]
#     filename_notes = note_dir[c_index]
#
#     sept_run_dir = single_experiment_processed.run(data_c, c_index)
qcm_dir, note_dir = load_data("data")
def new_experiments(qcm_dir):
    # if dataset in qcm_dir:
    #     return qcm_dir[dataset]
    # else:
    #     print(f"Dataset '{dataset}' not found in qcm_dir.")
    #     return None
    # experiments = []

    c = 0

    for file_name in qcm_dir:  # Use a different variable name here
        # Assuming single_experiment_processed.run returns an Experiment object
        c += 1
        exp = single_experiment_processed.run(file_name, c)

        # Manually add additional information for each experimental day
        exp.septin = input(f"Enter septin information for {file_name}: ")
        exp.gtp = input(f"Enter GTP information for {file_name}: ")

        experiments.append(exp)

    return experiments

print(new_experiments("20230718_qcm_sept_slb.csv"))
