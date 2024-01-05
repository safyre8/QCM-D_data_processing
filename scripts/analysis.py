import pandas as pd
from scripts.processing import single_experiment_processed

filename = "20230718_qcm_sept_slb.csv"
c = 1

sept_run_dir = single_experiment_processed.run(filename, c)
print(sept_run_dir)
print(list(sept_run_dir))
# # List to store 'time (min)' column data for each overtone
# time_min_columns = []
#
# # Access 'time (min)' column for each overtone and store them in a list
# for overtone, df in sept_run_dir.items():
#     time_min_column = df['time (min)']
#     time_min_columns.append(time_min_column)
#
# # Print the 'time (min)' columns for each overtone
# for overtone, time_min_column in zip(sept_run_dir.keys(), time_min_columns):
#     print(f"Time (min) for overtone {overtone}:\n{time_min_column}")

def soft_p(dataset: pd.DataFrame):
    # data_dir =
    # find the first and last value. subtract them
    time_df = dataset['time (min)']

    #Average the last 10 values to get the average across the dataset
    last_f_values = dataset['f (Hz)'].iloc[-5:]
    last_d_values = dataset['d (ppm)'].iloc[-5:]

    f_delta = dataset['f (Hz)'].iloc[:-1] - last_f_values.mean()
    d_delta = dataset['d (ppm)'].iloc[:-1] - last_d_values.mean()

    soft = d_delta / - f_delta
    new_table = pd.DataFrame({
        'Time': time_df,
        'Soft': soft
    })
    return new_table
# divid the f and d
soft_runner = soft_p(sept_run_dir)
print(soft_runner)
#
# soft_para_dir = {}
#
# # Iterate through different n values
# for n in n_values:
#     load = single_experiment_processed.run(filename, c, n)
#     result = soft_p(load)
#     soft_para_dir[n] = result
#     for key in soft_para_dir.keys():
#         print(key)
#         # print(qcm_dir[key].head(1))
#     print()
#     print(f"Result for n = {n}:", result)
# # df = single_experiment_processed.run(filename, c, n)
# # print(soft_p(df))
# # print(soft_p(filename, c, n))

#TODO: check this. I don't trust it.
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
