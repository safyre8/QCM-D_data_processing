import os
import sys
# import numpy as np
import pandas as pd

"""the function will load the files from the data folder as either 
    qcm-d experiment in the "qcm_dir" or as a note file in the "note_dir"""""

def load_data(folder_dir):
    all_files = os.listdir(os.path.normpath(sys.path[1] + "/" + folder_dir))  # check that the system path is correct

    # check the number of files with the tags
    note_files = list(filter(lambda f: f.endswith('_notes.csv'), all_files))
    qcm_txt_files = list(filter(lambda f: f.endswith('_slb.csv'), all_files))
    num_note_files = len(note_files)
    num_qcm_files = len(qcm_txt_files)
    print("==== Found {} QCM-D and {} note file(s) in {} folder! ====".format(num_qcm_files, num_note_files, folder_dir))

    qcm_dir = {}  # tag slb is for the support lipid bilayer
    note_dir = {}  # tag note is for the notes taken during the experiments

    # goes through the files in the data folder to add them to the empty directories above
    for file_name in all_files:
        if file_name.endswith("_slb.csv"):
            q_data_table = pd.read_csv(os.path.join(folder_dir, file_name), delimiter=",")
            qcm_dir[file_name] = q_data_table
            # for key in qcm_dir.keys():
            #     print(key)
            #     # print(qcm_dir[key].head(1))
            # print()

        if file_name.endswith("_notes.csv"):
            n_data_table = pd.read_csv(os.path.join(folder_dir, file_name), delimiter=",")
            note_dir[file_name] = n_data_table

    # checks the number of files in the directories to be able to compare to the number of files in the data folder
    num_qcm_dir = len(qcm_dir)
    num_note_dir = len(note_dir)
    print("==== Found {} QCM-D and {} note file(s) in the directories! ====".format(num_qcm_dir, num_note_dir))

    return qcm_dir, note_dir
#TODO: clean up the output by figuring out how to prevent the printing of all the now open files

# load_data("data")


print("==== Loaded the experimental and note files! ====")