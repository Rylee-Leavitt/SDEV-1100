#
# Rylee Leavitt
# 1/26/2025, 2/28/25,
# SDEV1100 1st project
# SDEV 1100
#

# Module 3 Assignment: Pseudo Code 1/26/2025
    # write as much pseudo code as you can for this project. 

# Import necessary libraries
#Library/Module Imports: Project Pt. 1 2/28/2025

from flask import Flask
app = Flask (__name__)

import pandas as pd #imports the pandas library with the alias pd
import os #imports the os module

# FOR each directory below the current one,
    #standardize each file in the directory
def standardize_excel_file(file_path, column_order):
    #Two parameters:
        #file_path: The path to the Excel file to be processed.
        #column_order: A list specifying the desired order of columns in the DataFrame.

    # Read the Excel file
        #reads the Excel file located at file_path into a pandas DataFrame df.
        #The pd.read_excel function is used to read the data from the Excel file.
    df = pd.read_excel(file_path)
    
    # Standardize column order
        #reorders the columns of the DataFrame df
        #based on the list column_order
    df = df[column_order]
    
    return df
    #return the Data Frame

def process_all_excel_files(input_directory, output_csv_path, column_order):
    #parameters:
        #input_directory.
        #output_csv_path
        #column_order

    # List all Excel files in the directory
    excel_files = [f for f in os.listdir(input_directory) if f.endswith('.xlsx')]
        #os.listdir(input_directory): 
            # uses the os module to list all the files and directories in the specified input_directory

        #if f.endswith('.xlsx')]:
            #checks if the file name ends with .xlsx (Excel file)

        #excel_files = :
            #assigns the list of Excel files to the variable excel_files

    # Initialize an empty DataFrame to hold all standardized data
    combined_df = pd.DataFrame(columns=column_order)
    
    for excel_file in excel_files:
        #starts a for loop that iterates over each file in the excel_files list

        file_path = os.path.join(input_directory, excel_file)
        #combining the input_directory path with the excel_file name. 
        #The os.path.join function ensures that the path is correctly formatted for the operating system.

        df = standardize_excel_file(file_path, column_order)
        #calls the standardize_excel_file function, 
        # passing the constructed file_path and column_order as arguments.

        combined_df = pd.concat([combined_df, df], ignore_index=True)
        #link standardized DataFrame (df) with the existing combined_df DataFrame.
        #ignore_index=True parameter ensures that the index is reset after linking, 
            #the index(s) are organized in order

    # Write the combined DataFrame to a CSV file
    combined_df.to_csv(output_csv_path, index=False)

# Example usage
input_directory = 'path/to/excel/files'             #defines the path to the directory containing the Excel files
output_csv_path = 'output/standardized_data.csv'    #defines the path and name of the output CSV file
column_order = ['Temperature', 'FlowRate', 'Pressure', 'OtherData']  # Replace with actual column names

process_all_excel_files(input_directory, output_csv_path, column_order)
#function with the specific input and output paths and desired column order
