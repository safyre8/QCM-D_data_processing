import pandas as pd
from scripts.processing import single_experiment_processed

filename = "20230718_qcm_sept_slb.csv"
c = 1

sept_run_dir = single_experiment_processed.run(filename, c)
# print(sept_run_dir)
# print(list(sept_run_dir))



def soft_p(dataset: pd.DataFrame):
    # find the first and last value. subtract them
    time_df = dataset.iloc[:, 1]
    # print(time_df)
    f_df = dataset['f (Hz)']
    d_df = dataset['d (ppm)']
    # print(f_df)

    #Average the last 10 values to get the average across the dataset
    last_f_values = dataset['f (Hz)'].iloc[-5:]
    last_d_values = dataset['d (ppm)'].iloc[-5:]

    f_delta = dataset['f (Hz)'].iloc[:-1] - last_f_values.mean()
    d_delta = dataset['d (ppm)'].iloc[:-1] - last_d_values.mean()

    soft = d_delta / - f_delta
    new_table = pd.DataFrame({
        'Time': time_df,
        'Soft': soft,
        'f (Hz)': f_df,
        'd (ppm)': d_df
    })
    return new_table

# # Iterate through the keys (overtones) in sept_run_dir
# for overtone in [3, 5, 7]:
#     # Check if the overtone exists in the directory
#     if overtone in sept_run_dir:
#         # Apply the soft_p function to the dataset corresponding to the overtone
#         soft_runner = soft_p(sept_run_dir[overtone])
#         print(f"Soft for overtone {overtone}:\n{soft_runner}")
#     else:
#         print(f"No data found for overtone {overtone}")

# soft_runner = soft_p(sept_run_dir[3])
# print(soft_runner)

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
