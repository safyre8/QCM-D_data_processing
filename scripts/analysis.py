import pandas as pd
from scripts.load_data import load_data
from scripts.processing import single_experiment_processed

# filename = "20230718_qcm_sept_slb.csv"
# c = 1
# n = 5
#
# result = single_experiment_processed.run(filename, c, n)
# print(result)

filename = "20230718_qcm_sept_slb.csv"
c = 1
n_values = [3, 5, 7]  # Different values of n to iterate over


def soft_p(dataset: pd.DataFrame):
    # find the first and last value. subtract them

    time_df = dataset.iloc[:, 0]

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


soft_para_dir = {}

# Iterate through different n values
for n in n_values:
    load = single_experiment_processed.run(filename, c, n)
    result = soft_p(load)
    soft_para_dir[n] = result
    for key in soft_para_dir.keys():
        print(key)
        # print(qcm_dir[key].head(1))
    print()
    print(f"Result for n = {n}:", result)
# df = single_experiment_processed.run(filename, c, n)
# print(soft_p(df))
# print(soft_p(filename, c, n))

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
