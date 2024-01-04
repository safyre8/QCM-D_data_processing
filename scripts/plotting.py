from scripts.load_data import load_data


qcm_dir, note_dir = load_data("data")

print(list(qcm_dir))

specific_qcm_data = qcm_dir['20230718_qcm_sept_slb.csv']


print(specific_qcm_data)
# print(load_data("data"))
# print(list(load_data("data")))
# print(qcm_dir.list)



