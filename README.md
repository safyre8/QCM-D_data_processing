# QCM-D_data_processing
 A project to plot the data from a QCM-D experiment

IMPORTANT: You need 2 files, ending with either "_slb" or "_notes". 
    "_slb" is the experimental data from the qcm-d.
    "_notes" is the notes taken during the experiment. 
        Contains two tags!!!
            1. SEPT_add (start the time series for where the protein is added)
            2. fb_wash (end the time series for the buffer wash)

1st: add the data files (as an excel or text file) to the data folder. 
    run the load scipt and run the function convert_files.
    This function will check all the files in the data folder and convert them into .csv.

For an overview of a single chamber experiment at overtones 3, 5, 7, and 9. 
    In the overview_single_experiment script, add the filename and chamber number
    Information you can get is 
        plots of:
            double axes with delta f and delta d;
            delta f; 
            delta d; 
            softness parameter (delta d/ -delta f)
        calculations of:
            softness parameter (delta d/ -delta f)
            Sauerbrey areal mass density 
            Sauerbrey thickness #still working on


To work with a file with a single chamber, overtone, with the selected data:
    Add filename and chamber to the processing script at the bottom.
    Uncomment out the sav_dir and saving information in the run function.
    run through all your chambers per file.
    comment out the sav_dir and saving information
    