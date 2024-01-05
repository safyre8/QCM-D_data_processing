import pandas as pd
import numpy as np

from scripts.load_data import load_data
from scripts.processing import single_experiment_processed
from scripts.analysis import soft_p
qcm_dir, note_dir = load_data("data")

print(list(qcm_dir))

filename = "20230718_qcm_sept_slb.csv"
c = 1
sept_run_dir = single_experiment_processed.run(filename, c)
soft_runner = soft_p(sept_run_dir[3])
print(soft_runner.keys())

# # Iterate through the files in the directory
# hex_files = []  # To store files with "hex" in the filename
# oct_files = []  # To store files with "oct" in the filename
#
# for filename in file_d:
#     if "hex" in filename:
#         hex_files.append(filename)
#     if "oct" in filename:
#         oct_files.append(filename)


# print(hex_files)


def plot_soft(filename: pd.DataFrame):
    """"Will plot an individual file for the softness parameters vs delta F"""
    # to sort the files as hexamers or octamers
    # id_h = 'hex'
    # id_o = 'oct'

    sept_run_dir = single_experiment_processed.run(filename, c)
    soft_df = soft_p(sept_run_dir[3])
    # load in the dataframe
    # df = time_zero(filename)

    # # calculate the softness parameter by the ratio (change in d)/(change of f)
    # df_soft = qcm_dir[filename]
    # soft_cal = df_soft['d (ppm)'] / -df_soft['f (Hz)']

    # plot the softness over -change of f
    x = soft_df['f (Hz)'][1:]
    y = soft_df[1:]
    fig, ax = plt.subplots()

    # customization of the plot

    ax.set_xlabel('-ΔF (Hz)')
    ax.set_ylabel('ΔD/-ΔF (Hz)', color='#000000')
    ax.plot(x, y, color='#000000', label=filename)
    ax.tick_params(axis='y', labelcolor='#000000')
    plt.xlim((0.0))
    plt.ylim((0, .5))

    # overall graph edits
    ax.legend()
    ax.grid(False)
    # save plot
    # plt.savefig(save_path + filename + '_softness.pdf', format='pdf')
    return soft_cal


plot_soft(filename)


# def plot_soft_dir(directory):
#     """"Will plot all the files in a directory for the softness parameters vs delta F"""
#     # to sort the files as hexamers or octamers
#     id_h = 'hex'
#     id_o = 'oct'
#
#     # make the figure to plot the files
#     fig, ax = plt.subplots()
#
#     # color_index = 0
#
#     for filename in qcm_dir:
#
#         if filename.endswith('.csv') and id_h in filename:
#             # load the file from the directory. The second converts the time and corrects the frequency to start at zero.
#             df = time_zero(filename)
#             df_soft = qcm_dir[filename]
#
#             # set x as the - frequency
#             x = - df['f (Hz)']
#
#             # calculate the softness parameter through the ratio of D/f
#             soft_cal = df_soft['d (ppm)'] / -df_soft['f (Hz)']
#             y = soft_cal
#
#             # plot the line
#             ax.plot(x, y, color='#FFFFFF', label="hexamers")
#             # 551A8B
#
#         if filename.endswith('.csv') and id_o in filename:
#             # load the file from the directory. The second converts the time and corrects the frequency to start at zero.
#             df_soft = qcm_dir[filename]
#             df = time_zero(filename)
#
#             # set x as the - frequency
#             x = - df['f (Hz)']
#
#             # calculate the softness parameter through the ratio of D/f
#             soft_cal = df_soft['d (ppm)'] / -df_soft['f (Hz)']
#             y = soft_cal
#             ax.plot(x, y, color='#FFFFFF', linestyle='-.', label="octamers")
#             # EE82EE
#
#         else:
#             # load the file from the directory. The second converts the time and corrects the frequency to start at zero.
#             df_soft = qcm_dir[filename]
#             df = time_zero(filename)
#
#             # set x as the - frequency
#             x = - df['f (Hz)']
#
#             # calculate the softness parameter through the ratio of D/f
#             soft_cal = df_soft['d (ppm)'] / -df_soft['f (Hz)']
#             y = soft_cal
#             ax.plot(x, y, color='#000000', linestyle='-.', label="n")
#
#     # customization of the plot
#     ax.set_xlabel('-ΔF (Hz)')
#     ax.set_ylabel('ΔD/-ΔF (Hz)')
#     ax.grid(False)
#     plt.xlim((0, 45))
#     plt.ylim((0, .31))
#     ax.legend()
#
#     plt.savefig(save_path + 'soft_se_45min.pdf', format='pdf')
#     return plt.show()
#
#
# plot_soft_dir(qcm_dir)
#
#
# def plot_double_y_data(filename: pd.DataFrame):
#     """Plots the data with the time vs frequency and dissipation for 1 dataset"""
#     df = time_zero(filename)
#
#     # name of axises
#     x = df['time (min)']  # time
#     data1 = df['f (Hz)']  # frequency
#     data2 = df['d (ppm)']  # dissipation
#
#     # Create a figure and two axes
#     fig, ax1 = plt.subplots()
#
#     # Plot data1 on the first y-axis (left)
#     color = 'tab:blue'
#     ax1.set_xlabel('Time (min)')
#     ax1.set_ylabel('ΔF (Hz)', color=color)
#     ax1.plot(x, data1, color=color)
#     ax1.grid(False)
#     ax1.tick_params(axis='y', labelcolor=color)
#
#     # Create a second y-axis (right) and plot data2 on it
#     ax2 = ax1.twinx()  # Share the same x-axis
#     color = 'tab:red'
#     ax2.set_ylabel('ΔD (ppm)', color=color)
#     ax2.plot(x, data2, color=color)
#     ax2.grid(False)
#     ax2.tick_params(axis='y', labelcolor=color)
#
#     # save the plot as a jpeg in equalibrium file
#     # plt.savefig(save_path + filename + '.jpg', format='jpeg')
#
#     return plt.show()
#
#
# # plot_double_y_data("20230718_c4_qcm_oct_slb.csv")
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
