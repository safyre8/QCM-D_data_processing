# QCM-D_data_processing
 A project to plot the data from a QCM-D experiment

The data is loaded as a .csv or .txt file. For now it's as a csv file set-up from the QCM-D from Leeds.


How to call processing script:

filename = "your_file_name.csv"

Chamber (c) can be called. The number of chamber is 1, 2, 3, 4. 
c = 1

df = single_experiment_processed.run(filename, c)

The overtone 3, 5, or 7 can be called from the run function. 
print(df[3])