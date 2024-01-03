from scripts.load_data import load_data


qcm_dir, note_dir = load_data("data")

print(list(qcm_dir))
specific_qcm_data = qcm_dir["S1_20230523_d-h-hex-50nm_1-ps_4-pip_slb.txt"]
print(specific_qcm_data)
# print(load_data("data"))
# print(list(load_data("data")))
# print(qcm_dir.list)



