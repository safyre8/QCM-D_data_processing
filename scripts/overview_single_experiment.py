from scripts.processing import single_experiment_processed
import scripts.analysis as analysis
import scripts.plotting as plotting



# """"running for a single file with the overtones from the data file""""
filename = "20230718_qcm_sept_slb.csv"
c = 1 #change for chamber [1, 2, 3, 4]
sept_run_dir = single_experiment_processed.run(filename, c)
n_values = [3, 5, 7, 9]

# print(analysis.soft_p(sept_run_dir))
print(analysis.soft_p_overall(sept_run_dir, n_values))
# print(analysis.Sauerbrey_M_overall(sept_run_dir[5], c))
# print(analysis.Sauerbrey_M_change(sept_run_dir[5], c))
# print(analysis.soft_p(sept_run_dir))


# """"running for a single file with the overtones.""""
plotting.plot_double_y_data(sept_run_dir[5]) #overtone [3, 5, 7, 9]

plotting.plot_d(sept_run_dir)
plotting.plot_f(sept_run_dir)

sept_soft_dir = analysis.soft_p(sept_run_dir)
plotting.plot_soft(sept_soft_dir)