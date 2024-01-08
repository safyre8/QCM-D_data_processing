import pandas as pd
import numpy as np
from scripts.load_data import load_data

# TODO: make it so that all the chambers can be pulled out
# TODO: make a directory to save all these files. Then average them.
# TODO: can I make a table with all the saved information about the chambers.
# TODO: GTP +/- ; SEPT (HEX/OCT) ; SOFTNESS PARAMETER; BINDING KINETICS ; THICKNESS; AMD (QCM-D)
# TODO: make sure that the headers are saved in the equialibrium file
# TODO: do all the data for the datasets



# Set variables for the (c) chamber:int. The overtones are set for 3, 5, and 7.

class single_experiment_processed:
    """" this class will run with one chamber and overtone number for a single file.
    will take a data file and the matching note file to filter,
    average the solution,
    and select the time from adding septins to washing"""

    def __init__(self, dataset: str, c: int):
        """runs the script, making the final changes to set the time to start at zero and remove the slb signal from the frequency"""
        qcm_dir, note_dir = load_data("data")
        self.data = qcm_dir[dataset]
        c = c
        self.process_n()
        self.filter_data()
        self.ave_slb_baseline()
        self.find_matching_notes()
        new_df = self.eq_time_select()


        return new_df
        # n_values = [3, 5, 7, 9]
        #
        # sept_run_dir = {}
        #
        # # Iterate through different n values
        # for n in n_values:
        #     data = self.eq_time_select()
        #     time_zero = data.iloc[:, 0] - data.iloc[0, 0]
        #     freq_zero = data.iloc[:, 1] - data.iloc[1, 1]
        #     de_set = data.iloc[:, 2]
        #     final_table = pd.DataFrame(data={
        #         'time (min)': time_zero,
        #         'f (Hz)': freq_zero,
        #         'd (ppm)': de_set
        #     })
        #     sept_run_dir[n] = final_table
        #     # print(f"Result for n = {n}:", final_table)
        # num = list(sept_run_dir)
        # print("==== Finished by converting the time and frequency to start at zero for overtones {}! ====".format(num))
        # return sept_run_dir
    def process_n(self):
        n_values = [3, 5, 7, 9]

        sept_run_dir = {}

        # Iterate through different n values
        for n in n_values:
            data = self.eq_time_select()
            time_zero = data.iloc[:, 0] - data.iloc[0, 0]
            freq_zero = data.iloc[:, 1] - data.iloc[1, 1]
            de_set = data.iloc[:, 2]
            final_table = pd.DataFrame(data={
                'time (min)': time_zero,
                'f (Hz)': freq_zero,
                'd (ppm)': de_set
            })
            sept_run_dir[n] = final_table
            # print(f"Result for n = {n}:", final_table)
        num = list(sept_run_dir)
        print("==== Finished by converting the time and frequency to start at zero for overtones {}! ====".format(num))
        return sept_run_dir

    def filter_data(self) -> pd.DataFrame:
        """Takes a csv file to seperate out the time(Time), frequency (f), and dissipation (D) for a chamber (c) at the Harmonic of interest (n) to give an array with these columns"""
        # load the dataframe from the experimental directory
        # self.data =  qcm_dir[dataset]
        data = self.data
        desired_columns = [
            f"Time_{c} [s]",
            f"f{n}_{c} [Hz]",
            f"D{n}_{c} [ppm]"
        ]
        filtered_table = new_df[desired_columns]
        print("==== Filtered for chamber {} and overtone {} in the file: '{}'! ====".format(c, n, dataset))
        return filtered_table


    def ave_slb_baseline(self, t_base_s: float = 6., t_base_e: float = 8.):
        """Takes the filtered dataset to convert the time from seconds to minutes and average the frequency and dissipation from the SLB baseline."""

        filter_data = self.filter_data()
        time_sec = filter_data.iloc[:, 0]  # takes the first row from the filter_data, which is always time
        time_min = (time_sec / 60).round(2)  # convert the time into minutes
        # print("==== Converted the time from seconds into minutes! ====")

        # set a range to find the average to normalize the frequency and dissipation channels across the entire dataset
        rows_in_range = (time_min >= t_base_s) & (time_min <= t_base_e)
        data_in_range = filter_data.loc[rows_in_range]

        f_avg = data_in_range.iloc[:, 1].mean()  # averaging over frequency
        d_avg = data_in_range.iloc[:, 2].mean()  # averaging over dissipation

        norm_f = (filter_data.iloc[:, 1] - f_avg) / 5  # 5 is the scaling for overtone 5
        norm_d = filter_data.iloc[:, 2] - d_avg

        norm_table = pd.DataFrame(data={
            'time (min)': time_min,
            'f (Hz)': norm_f,
            'd (ppm)': norm_d
        })
        print("==== Averaged the dataset from  {} to {} minutes for the ambient solution baseline! ====".format(t_base_s, t_base_e))
        return norm_table

    def find_matching_notes(self):
        """This will find the matching note file (_note) for the data file (_slb)"""
        note_file_name = self.replace("slb", f"notes")
        notes_file = note_dir[self.replace("slb", f"notes")]
        return notes_file, note_file_name

    def eq_time_select(self):
        """This function will take a data file, filtered and normalized, and the reference from the note file when septins are added (SEPT_add) and washed (fb_wash)"""
        # load and define the 2 datasets. The data file comes from the experimental data.
        data_file = self.ave_slb_baseline()
        notes_file, note_file_name = self.find_matching_notes()

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





qcm_dir, note_dir = load_data("data")
filename = "20230718_qcm_sept_slb.csv"
c = 1

sep_instance = single_experiment_processed(filename, c)
# result = sep_instance.eq_time_select()
print(result)