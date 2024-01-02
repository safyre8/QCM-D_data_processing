import os
import sys

def load_data(n):
    input_folder = os.path.join(os.path.normpath(sys.path[3]), "input")
    file_path = os.path.join(input_folder, str(n) + "_" + "theta" + ".txt")
    data = np.loadtxt(file_path, delimiter="\t")
    return data
    print("Data loaded")
load_data(0)

data_path = r"O:/PhD 2023/Data/qcm_se_all_excel/.csv/qcm/"  # data files, with colunms: time, f, d for x# of chambers
data_note_path = r"O:/PhD 2023/Data/qcm_se_all_excel/.csv/notes/"  # notes files, with columns: time (min),  pump, stirrer, solution (SEPT_add/fb_wash)

original_files = os.listdir(data_path)
original_note_files = os.listdir(data_note_path)

file_d = {}
file_note = {}

for file_name in original_files:
    data_table = pd.read_csv(data_path + file_name)
    file_d[file_name] = data_table
    for key in file_d.keys():
        print(key)
        print(file_d[key].head(4))
    print()

for file_note_name in original_note_files:
    data_note_table = pd.read_csv(data_note_path + file_note_name)
    file_note[file_note_name] = data_note_table
    for key in file_note.keys():
        print(key)
        print(file_note[key].head(4))

# present clear output from the imported data
for key in file_d.keys():
    print(key)
    print(file_d[key].head(4))
    print()

