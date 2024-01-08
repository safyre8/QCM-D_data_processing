import pandas as pd
from scripts.processing import single_experiment_processed

filename = "20230718_qcm_sept_slb.csv"
c = 1

sept_run_dir = single_experiment_processed.run(filename, c)
# print(sept_run_dir)
# print(list(sept_run_dir))

import pandas as pd

filename = "20230718_qcm_sept_slb.csv"
c = 1

sept_run_dir = single_experiment_processed.run(filename, c)

n_values = [3, 5, 7, 9]
soft_para_dir = {}

def soft_p(dataset: pd.DataFrame):
    for overtone in n_values:
        if overtone in dataset:
            time_df = dataset[overtone]['time (min)']
            f_df = dataset[overtone]['f (Hz)']
            d_df = dataset[overtone]['d (ppm)']

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
                'd (ppm)': d_df
            })
            soft_para_dir[overtone] = new_table
            print(f"Soft for overtone {overtone}:\n{soft}")  # Print softness values for current overtone
        else:
            print(f"No data found for overtone {overtone}")

    return soft_para_dir

soft_runner = soft_p(sept_run_dir)
print(soft_runner)


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
