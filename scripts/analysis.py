import pandas as pd
from scripts.processing import single_experiment_processed

filename = "20230718_qcm_sept_slb.csv"
c = 1

sept_run_dir = single_experiment_processed.run(filename, c)
# print(sept_run_dir)
# print(list(sept_run_dir))

import pandas as pd

filename = "20230718_qcm_sept_slb.csv"
c = 4

sept_run_dir = single_experiment_processed.run(filename, c)

n_values = [3, 5, 7, 9]
soft_para_dir = {}

def soft_p(dataset: pd.DataFrame):
    for overtone in n_values:
        if overtone in dataset:
            time_df = dataset[overtone]['time (min)']
            f_df = dataset[overtone]['f (Hz)']
            d_df = dataset[overtone]['d (ppm)']* 10**-6

            last_f_values = f_df.iloc[-5:]
            last_d_values = d_df.iloc[-5:]

            f_delta = f_df.iloc[:-1] - last_f_values.mean()
            d_delta = d_df.iloc[:-1] - last_d_values.mean()
            divid_f = -f_delta / overtone

            soft = d_delta / divid_f
            new_table = pd.DataFrame({
                'time (min)': time_df,
                'Soft': soft,
                'f (Hz)': f_df,
                'd (10^-6)': d_df
            })
            soft_para_dir[overtone] = new_table
            print(f"Soft for overtone {overtone}:\n{soft}")  # Print softness values for current overtone
        else:
            print(f"No data found for overtone {overtone}")

    return soft_para_dir

soft_runner = soft_p(sept_run_dir)
print(soft_runner)


def soft_p_overall(dataset: pd.DataFrame, n_values):
    """Calculate the criterion to determine if the film is sufficently thin for the Sauerbrey equation"""

    soft_per_overtone = {}

    for overtone in n_values:
        if overtone in dataset:
            #select the columns for the frequency and disipation
            f_df = dataset[overtone]['f (Hz)']
            d_df = dataset[overtone]['d (ppm)'] * 10**-6
            print(d_df)

            #select the first value of each column
            first_f_value = f_df.iloc[0]
            first_d_value = d_df.iloc[0]

            #sum the last 5 values for each column
            last_f_values = sum(f_df.iloc[-5:]) / 5
            last_d_values = sum(d_df.iloc[-5:]) / 5

            #calculate the difference between the first value and the average of the last 5
            f_delta = last_f_values - first_f_value
            d_delta = last_d_values - first_d_value

            #calculate the criterion for each overtone
            divid_f = f_delta / overtone
            soft = d_delta / - divid_f
            soft_per_overtone[overtone] = soft
        else:
            print(f"No data found for overtone {overtone}")

    return soft_per_overtone

soft_num = soft_p_overall(sept_run_dir, n_values)
print(soft_num)


def Sauerbrey_M(dataset: pd.DataFrame, c, n):
    """Areal mass density from the QCM-D"""
    df = single_experiment_processed.run(dataset, c, n)
    SC = 18 #ng/(cm2∙ Hz) is the mass sensitivity constant for a 5 MHz crystal

    last_f_values = df['f (Hz)'].iloc[-5:]
    print(last_f_values)
    f_delta = df['f (Hz)'].iloc[-1] - last_f_values.mean()
    print(f_delta)
    return -SC * f_delta/n

# print(Sauerbrey_M(filename, c, n))
