import pandas as pd
import numpy as np
from scripts.load_data import load_data

qcm_dir, note_dir = load_data("data")

#Set variables for the (c) chamber:int and (n) overtone:int
c = 2
n = 5

# print(list(qcm_dir))
filename = "20230718_qcm_sept_slb.csv"

specific_qcm_file = qcm_dir["20230718_qcm_sept_slb.csv"]
# print(specific_qcm_file)
# print(specific_qcm_file.keys())
# class single_experiment_processed:
#
#     # """" this class will run with one chamber and overtone number for a single file.
#     will take a data file and the matching note file to filter,
#     average the solution,
#     and select the time from adding septins to washing"""
#     # %%
def filter_data(dataset: pd.DataFrame) -> pd.DataFrame:
    """Takes a csv file to seperate out the time(Time), frequency (f), and dissipation (D) for a chamber (c) at the Harmonic of interest (n) to give an array with these columns"""

    desired_columns = [
        f"Time_{c} [s]",
        f"f{n}_{c} [Hz]",
        f"D{n}_{c} [ppm]"
    ]
    filtered_table = dataset[desired_columns]

    print("==== Filtered for chamber {} and overtone {} in the file: '{}'! ====".format(c, n, filename))
    return filtered_table

#
# filter_c = filter_data(specific_qcm_file)
#
#
# # %%
def ave_slb_baseline(dataset: pd.DataFrame, t_base_s: float = 6., t_base_e: float = 8.):
    """Takes the filtered dataset to convert the time from seconds to minutes and average the frequency and dissipation from the SLB baseline."""

    time_sec = dataset.iloc[:, 0]  # takes the first row from the filter_data, which is always time
    time_min = (time_sec / 60).round(2)  # convert the time into minutes
    print("==== Converted the time from seconds into minutes! ====")

    # set a range to find the average to normalize the frequency and dissipation channels across the entire dataset
    rows_in_range = (time_min >= t_base_s) & (time_min <= t_base_e)
    data_in_range = dataset.loc[rows_in_range]

    # TODO: Set a if and else statement for if the data is properly selected to find the averages/no data if found
    # if data_in_range[]:

    f_avg = data_in_range.iloc[:, 1].mean()  # averaging over frequency
    d_avg = data_in_range.iloc[:, 2].mean()  # averaging over dissipation
    # else:
    # #     print ("zero rows in range")
    norm_f = (dataset.iloc[:, 1] - f_avg) / 5  # 5 is the scaling for overtone 5
    norm_d = dataset.iloc[:, 2] - d_avg

    norm_table = pd.DataFrame(data={
        'time (min)': time_min,
        'f (Hz)': norm_f,
        'd (ppm)': norm_d
    })
    print("==== Averaged the dataset from  {} to {} minutes for the ambient solution baseline! ====".format(t_base_s, t_base_e))
    return norm_table

def find_matching_notes(file_name: str):
    """This will find the matching note file (_note) for the data file (_slb)"""

    note_file_name = file_name.replace("slb", f"notes")
    notes_file = note_dir[file_name.replace("slb", f"notes")]
    return notes_file, note_file_name
# c_value = 1  # Define c here or get it from somewhere
# filename = "20230718_qcm_sept_slb.csv"
# matching_notes = find_matching_notes(filename)
# print(matching_notes)


def eq_time_select(file_name: pd.DataFrame):
    """This function will take a data file, filtered and normalized, and the reference from the note file when septins are added (SEPT_add) and washed (fb_wash)"""
    # load and define the 2 datasets. The data file comes from the experimental data.
    data_file = ave_slb_baseline(filter_data(specific_qcm_file))
    notes_file, note_file_name = find_matching_notes(file_name)

    # find the string of "SEPT_add" or "fb_wash" in the note dataframe to indicate the row that septins are add or washed
    condition_add = (notes_file['solution'] == "SEPT_add")
    condition_wash = (notes_file['solution'] == "fb_wash")
    # # The row that is noted from the pervious call
    index_add = notes_file.index[condition_add].tolist()
    index_wash = notes_file.index[condition_wash].tolist()
    # Find the time in the row with the solution as "SEPT_add" or "fb_wash"
    SEPT_s = notes_file.loc[index_add[0], 'time (min)']
    SEPT_e = notes_file.loc[index_wash[0], 'time (min)']

    n_SEPT_s = pd.to_numeric(SEPT_s)
    n_SEPT_e = pd.to_numeric(SEPT_e)

    filtered_df2 = data_file[(data_file['time (min)'] >= n_SEPT_s) & (data_file['time (min)'] <= n_SEPT_e)]
    print("==== Selected the data from the notes file for when protein (SEPT) was added to wash! ====")
    return filtered_df2


print(eq_time_select(filename))


# THIS WORKS FOR THE MULTIPLE CHANNELS!!!!!!!!!!!!
# def run(work_file_name: str, c, n, sept_base_s: float = 6., sept_base_e: float = 8.):
#     """This will take a data file and the matching note file to filter, average the solution, and select the time from adding septins to washing"""
#
#
#     # file_load = pd.read_csv(data_path + work_file_name)  # load dataframe
#     filtered = filter_data(work_file_name)  # filter for specific overtone and chamber
#     # TODO: check that the baseline can change according to the notefile...
#     base_data = ave_slb_baseline(filtered)  # normalize to a baseline
#
#     equal_sept = eq_time_select(work_file_name, n,
#                                 c)  # selects for the time after septins are added to when they are washed
#     return equal_sept
#
#
# f_septin_time("20220920_all_n.csv", 5, 2)

# TODO: make it so that all the chambers can be pulled out
# TODO: make a directory to save all these files. Then average them.
# TODO: can I make a table with all the saved information about the chambers.
# TODO: GTP +/- ; SEPT (HEX/OCT) ; SOFTNESS PARAMETER; BINDING KINETICS ; THICKNESS; AMD (QCM-D)
# TODO: make sure that the headers are saved in the equialibrium file


# TODO: do all the data for the datasets
