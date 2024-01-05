from scripts.load_data import load_data
from scripts.processing import single_experiment_processed
from scripts.analysis import soft_p
qcm_dir, note_dir = load_data("data")

print(list(qcm_dir))

# filename = "20230718_qcm_sept_slb.csv"
# c = 1
# n = 5
#
# # result = single_experiment_processed.run(filename, c, n)
# # print(result)
#
# soft_result = soft_p(filename, c, n)
# print(soft_result)

filename = "20230718_qcm_sept_slb.csv"
c = 1

df = single_experiment_processed.run(filename, c)
print(df)

