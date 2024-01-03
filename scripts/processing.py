import pandas as pd
import numpy as np
from scripts.load_data import load_data

qcm_dir, note_dir = load_data("data")


# print(list(qcm_dir))
# specific_qcm_data = qcm_dir["S1_20230523_d-h-hex-50nm_1-ps_4-pip_slb.txt"]
# print(specific_qcm_data)
# print(specific_qcm_data.keys())
#
def filter_data(dataset: pd.DataFrame, overtone: int, chamber: int) -> pd.DataFrame:
    """Takes a csv file to seperate out the time(Time), frequency (f), and dissipation (D) for a chamber (c) at the Harmonic of interest (n) to give an array with these columns"""

    n = overtone
    c = chamber
    #        f"Time_{c} [s]", f"F_{n}:{c} [Hz]", f"D_{n}:{c} [ppm]

    desired_columns = [
        f"Time_{c}",
        f"F_{c}:{n}",
        f"D_{c}:{n}"
    ]
    filtered_table = dataset[desired_columns]
    return filtered_table

# # can filter out an overtone, chamber for dataset
# # TODO: this only works for chamber 1
# # set the filtered data for overtone and channel to the working data for math (dm). Overtones are only odd.
working_file = qcm_dir["S1_20230523_d-h-hex-50nm_1-ps_4-pip_slb.txt"]
# filter_c = filter_data(working_file, 5, 1)
# print(filter_c)

#changed from normalized_data
def average_data(dataset: pd.DataFrame, t_base_s: float = 6., t_base_e: float = 8.):
    """Takes the filtered dataset to convert the time from seconds to minutes and average the frequency and dissipation from the SLB baseline."""

    Time_sec = dataset.iloc[:, 0]  # takes the first row from the filter_data, which is always time
    Time_min = (Time_sec / 60).round(2)  # convert the time into minutes
    # set a range to find the average to normalize the frequency and dissipation channels across the entire dataset
    rows_in_range = (Time_min >= t_base_s) & (Time_min <= t_base_e)
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

    return norm_table

# # normalize the dataset that was selected for
#
# normalized_data(filter_data(file_d["n_20221006_slb.csv"], 5, 1))
# norm_data = normalized_data(filter_c)
print(average_data(filter_data(working_file, 5, 1)))



