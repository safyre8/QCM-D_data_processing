import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# import matplotlib.cm as cm
# from matplotlib import colormaps
# print(list(colormaps))

from scripts.load_data import load_data
from scripts.processing import single_experiment_processed
from scripts.analysis import soft_p

qcm_dir, note_dir = load_data("data")
# print(qcm_dir)
# print(list(qcm_dir))

filename = "20230718_qcm_sept_slb.csv"
c = 1
n_values = [3, 5, 7, 9]
sept_run_dir = single_experiment_processed.run(filename, c)
sept_soft_dir = soft_p(sept_run_dir)
# print(sept_soft_dir)



def plot_f(directory):
    """"Will plot all the files in a directory for the softness parameters vs delta F"""
    # Create a figure to plot the files
    fig, ax = plt.subplots()
    cmap = plt.get_cmap("Blues")
    color_index = 1

    for n, df in directory.items():
        x = df['time (min)']
        y = -df['f (Hz)']

        color_index += 1
        color = cmap(color_index / len(directory))
        # Plot the line
        ax.plot(x, y, color=color, label=f"Overtone {n}")

    # Customization of the plot
    ax.set_xlabel('Time (min)')
    ax.set_ylabel('-ΔF (Hz)')  # Make sure this label corresponds to the data
    ax.grid(False)
    plt.xlim((0))
    plt.ylim((0))
    ax.legend(loc='lower right')

    # plt.savefig(save_path + 'all_combined_qcm-d.pdf', format='pdf')
    plt.show()

# plot_f(sept_soft_dir)

def plot_d(directory):
    """"Will plot all the files in a directory for the softness parameters vs delta F"""
    # Create a figure to plot the files
    fig, ax = plt.subplots()
    cmap = plt.get_cmap("Reds")
    color_index = 1

    for n, df in directory.items():
        x = df['time (min)']
        y = df['d (ppm)']

        color_index += 1
        color = cmap(color_index / len(directory))
        # Plot the line
        ax.plot(x, y, color=color, label=f"Overtone {n}")

    # Customization of the plot
    ax.set_xlabel('Time (min)')
    ax.set_ylabel('-ΔD (ppm)')
    ax.grid(False)
    plt.xlim((0))
    plt.ylim((0))
    ax.legend(loc='lower right')

    # plt.savefig(save_path + 'all_combined_qcm-d.pdf', format='pdf')
    plt.show()

# plot_d(sept_run_dir)


# print(soft_runner.keys())

# # Iterate through the files in the directory
# hex_files = []  # To store files with "hex" in the filename
# oct_files = []  # To store files with "oct" in the filename
#
# for filename in file_d:
#     if "hex" in filename:
#         hex_files.append(filename)
#     if "oct" in filename:
#         oct_files.append(filename)

#     # to sort the files as hexamers or octamers
#     id_h = 'hex'
#     id_o = 'oct'

# print(hex_files)


def plot_soft(directory):
    """"Will plot an individual file for the softness parameters vs delta F"""

    fig, ax = plt.subplots()
    cmap = plt.get_cmap("Reds")
    color_index = 0

    for n, df in directory.items():
        print(df.columns)
        x = - df['f (Hz)']
        y = df['Soft']

        color_index += 1
        color = cmap(color_index / len(directory))
        # Plot the line
        ax.plot(x, y, color=color, label=f"Overtone {n}")

    # customization of the plot
    ax.set_xlabel('-ΔF (Hz)')
    ax.set_ylabel('ΔD/(-ΔF/n) (Hz)')
    ax.plot(x, y, color='#000000')
    # ax.plot(x, y, color='#000000', label=filename)
    # ax.tick_params(axis='y')
    plt.xlim((0.0))
    plt.ylim((0))

    # overall graph edits
    ax.grid(False)
    ax.legend(loc='lower right')
    plt.show()
    # save plot
    # plt.savefig(save_path + filename + '_softness.pdf', format='pdf')

plot_soft(sept_soft_dir)

def plot_double_y_data(filename: pd.DataFrame):
    """Plots the data with the time vs frequency and dissipation for 1 dataset"""
    # sept_run_dir = single_experiment_processed.run(filename, c)
    # soft_df = soft_p(sept_run_dir[7])

    # name of axises
    x = filename['time (min)']  # time
    data1 = filename['f (Hz)']  # frequency
    data2 = filename['d (ppm)']  # dissipation

    # Create a figure and two axes
    fig, ax1 = plt.subplots()

    # Plot data1 on the first y-axis (left)
    color = 'tab:blue'
    ax1.set_xlabel('Time (min)')
    ax1.set_ylabel('ΔF (Hz)', color=color)
    ax1.plot(x, data1, color=color)
    ax1.grid(False)
    ax1.tick_params(axis='y', labelcolor=color)

    # Create a second y-axis (right) and plot data2 on it
    ax2 = ax1.twinx()  # Share the same x-axis
    color = 'tab:red'
    ax2.set_ylabel('ΔD (ppm)', color=color)
    ax2.plot(x, data2, color=color)
    ax2.grid(False)
    ax2.tick_params(axis='y', labelcolor=color)

    # save the plot as a jpeg in equalibrium file
    # plt.savefig(save_path + filename + '.jpg', format='jpeg')

    return plt.show()

# plot_double_y_data(sept_run_dir_3)
#
#
# def plot_all(directory_path):
#     """This will take and plot all of the files in the directory if they are hexamers or octamers"""
#
#     # to sort the files as hexamers or octamers
#     id_h = 'hex'
#     id_o = 'oct'
#     # cmap = plt.get_cmap("BuPu")
#     # color = cmap(0)
#
#     fig, ax = plt.subplots()
#
#     color_index = 0
#
#     for filename in qcm_dir:
#
#         if filename.endswith('.csv') and id_h in filename:
#             df = time_zero(filename)
#             x = df['time (min)']
#             y = -df['f (Hz)']
#             # color = cmap(color_index / len(qcm_dir))
#             # color_index += 0
#             ax.plot(x, y, color='#551A8B', label="hexamer")
#
#         if filename.endswith('.csv') and id_o in filename:
#             df = time_zero(filename)
#             # label = filename[8]
#             x = df['time (min)']
#             y = -df['f (Hz)']
#
#             # color_index += 1
#             # color = cmap(color_index / len(qcm_dir))
#
#             ax.plot(x, y, color='#EE82EE', linestyle='-.', label="octamer")
#
#         # else:
#         #     color_index += 1
#     ax.set_xlabel('Time (min)')
#     ax.set_ylabel('-ΔF (Hz)')
#     ax.grid(False)
#     plt.xlim((0, 30))
#     plt.ylim((0))
#     ax.legend()
#
#     plt.savefig(save_path + 'all_qcm_se.pdf', format='pdf')
#     # plt.show()
#     return plt.show()
#
#     # return(plt)
#
#
# plot_all(qcm_dir)
#
#
# def plot_f(directory):
#     """"Will plot all the files in a directory for the softness parameters vs delta F"""
#     # to sort the files as hexamers or octamers
#     id_h = 'hex'
#     id_o = 'oct'
#
#     # make the figure to plot the files
#     fig, ax = plt.subplots()
#     cmap = plt.get_cmap("Blues")
#     color_hex = cmap(0.8)
#     color_oct = cmap(0.4)
#     # color = cmap(3)
#     # color_index = 0
#
#     for filename in qcm_dir:
#
#         if filename.endswith('.csv') and id_h in filename:
#             # load the file from the directory. The second converts the time and corrects the frequency to start at zero.
#             df = time_zero(filename)
#
#             x = df['time (min)']
#             y = -df['f (Hz)']
#
#             # plot the line
#             ax.plot(x, y, color=color_hex, label="hexamer")
#
#         if filename.endswith('.csv') and id_o in filename:
#             # load the file from the directory. The second converts the time and corrects the frequency to start at zero.
#             df = time_zero(filename)
#
#             x = df['time (min)']
#             y = -df['f (Hz)']
#             # plot the line
#             ax.plot(x, y, color=color_oct, label="octamer")
#
#     # customization of the plot
#     ax.set_xlabel('Time (min)')
#     ax.set_ylabel('-ΔF (Hz)')
#     ax.grid(False)
#     plt.xlim((0))
#     plt.ylim((0))
#     ax.legend()
#
#     plt.savefig(save_path + 'all_combined_qcm-d.pdf', format='pdf')
#     return plt.show()
#
#
# plot_f(qcm_dir)

