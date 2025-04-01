#
# Rylee Leavitt
# 3/5/2025
# SDEV1100 1st project
# SDEV 1100
#
#data_Extraction.py

import pandas as pd #imports the pandas library with the alias pd
import os #imports the os module

#create a pyhton program that can complete Data Extraction: (3/5/2025)
    #The system will read and access multiple Excel files located in a specified directory.
    #identifying and extracting relevant data fields
            #such as temperature, flow rate, pressure, and any other specified metrics.

def extract_data(directory, output_file):

    # Fields to extract (temperature, flow rate, pressure)
    relevant_fields = ['Temperature', 'Flow Rate', 'Pressure']

    # Create an empty DataFrame to store results
    extracted_data = pd.DataFrame()

    for filename in os.listdir(directory):
        #Creates a For loop that will iterate through all the files and folders located within a specified directory
        #ex) os.listdir("C:/Documents")

        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            # if the name of the file ends withb.xlsx (excel file)

            file_path = os.path.join(directory, filename)
            #generates the full path to the file
            #ex) C:/Documents/file1.xlsx

            print(f"Processing file: {filename}")
            #tells the user which file is processing
            
            # Read the Excel file
            try:
                #reads an Excel file and store its contents into a DataFrame (df)
                df = pd.read_excel(file_path)

                # Extract relevant fields
                filtered_data = df[relevant_fields]
                #This selects specific columns from the DataFrame

                filtered_data["Source_File"] = filename
                #adds the column Source_file
                    #helps us track what info was processd from each file
                    #the filename variable contains the name of the current Excel file being processed

                # Append to the main DataFrame
                extracted_data = pd.concat([extracted_data, filtered_data], ignore_index=True)
                #combining two DataFrames—extracted_data and filtered_data—into one
                #ignore_index=True resets the index of the combined DataFrame to a continuous range

            except Exception as e:
                print(f"Error processing file {filename}: {e}")
                #Tells the user when, and which file the error occured

    # Save the extracted data to a new CSV file
    extracted_data.to_csv(output_file, index=False)
    #This command writes the extracted_data DataFrame to a CSV file specified by the output_file variable.
    
    print(f"Data extraction complete. Results saved to {output_file}")
    #tells the user the extraction is complete and saved to a specific file

import sys
# Usage
directory = sys.argv[2]
#This line specifies the folder or directory where the Excel files are located.

output_file = sys.argv[1]
#This defines the name and location of the output file

extract_data(directory, output_file)
#calls the function
