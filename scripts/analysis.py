import pandas as pd


n_values = [3, 5, 7, 9]
def soft_p(dataset: pd.DataFrame):
    soft_para_dir = {}

    for overtone in n_values:
        if overtone in dataset:
            time_df = dataset[overtone]['time (min)']
            f_df = dataset[overtone]['f (Hz)']
            d_df = dataset[overtone]['d (ppm)']* 10**-6
            print(d_df)
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
            print(f_df)
        else:
            print(f"No data found for overtone {overtone}")

    return soft_para_dir

def soft_p_overall(dataset: pd.DataFrame, n_values):
    """Calculate the criterion to determine if the film is sufficently thin for the Sauerbrey equation"""

    soft_per_overtone = {}

    for overtone in n_values:
        if overtone in dataset:
            #select the columns for the frequency and disipation
            f_df = dataset[overtone]['f (Hz)']
            d_df = dataset[overtone]['d (ppm)']* 10**-6

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



def soft_p_overall(dataset: pd.DataFrame, n_values):
    """Calculate the criterion to determine if the film is sufficently thin for the Sauerbrey equation"""

    soft_per_overtone = {}

    for overtone in n_values:
        if overtone in dataset:
            #select the columns for the frequency and disipation
            f_df = dataset[overtone]['f (Hz)']
            d_df = dataset[overtone]['d (ppm)'] * 10**-6

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

def Sauerbrey_M_overall(dataset: pd.DataFrame, c):
    """Areal mass density from the QCM-D calculated from the change from first f value to average of last 50 values"""
    # df = single_experiment_processed.run(dataset, c)
    SC = 18 #ng/(cm2∙ Hz) is the mass sensitivity constant for a 5 MHz crystal

    last_f_values = dataset['f (Hz)'].iloc[-50:]

    f_delta =  last_f_values.mean() - dataset['f (Hz)'].iloc[1]

    return -SC * f_delta/5 #5 is the overtone



def Sauerbrey_M_change(dataset: pd.DataFrame, c):
    """Areal mass density from the QCM-D over time"""
    # df = single_experiment_processed.run(dataset, c)
    SC = 18 #ng/(cm2∙ Hz) is the mass sensitivity constant for a 5 MHz crystal
    f_delta = dataset['f (Hz)']
    return -SC * f_delta/5 #5 is the overtone



def Sauerbrey_H(dataset):
    SC = 18  # ng/(cm2∙ Hz) is the mass sensitivity constant for a 5 MHz crystal
    p = 1 # protein density
    f_delta = dataset['f (Hz)']
    return f_delta * -(SC/(5*p))