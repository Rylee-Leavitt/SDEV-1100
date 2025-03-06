#
# Rylee Leavitt
# 1/26/2025, 2/28/25, 3/5/2025
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

def extract_data_from_excel(directory, metrics):
    #Defines a function to extract data from the excel files

    #Reads Excel files in the specified directory and extracts specified metrics.
        #directory example) C:/MyFolder
        #metrics: temperature, flow rate, pressure
        #Returns pd.DataFrame: DataFrame containing the organized extracted data.

    extracted_data = []
    #initializes an empty list called extracted_data

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        #Creates a For loop that will iterate through all the files and folders located within a specified directory
        #ex) os.listdir("C:/Documents")

        if filename.endswith(".xlsx") or filename.endswith(".xls"):
            # if the name of the file ends withb.xlsx (excel file)

            filepath = os.path.join(directory, filename)
            #generates the full path to the file
            #ex) C:/Documents/file1.xlsx

            try:
                #reads an Excel file and store its contents into a DataFrame (df)
                df = pd.read_excel(filepath)

                # Filter relevant columns 
                filtered_data = df[metrics]
                #This selects specific columns from the DataFrame

                filtered_data["Source_File"] = filename
                #adds the column Source_file
                    #helps us track what info was processd from each file
                    #the filename variable contains the name of the current Excel file being processed

                extracted_data.append(filtered_data)
                #adds the filtered_data DataFrame to the end of the extracted_data list

            except Exception as e:
                # if an error occurs thr program jumps to except block

                print(f"Error processing file {filename}: {e}")
                #Tells the user when, and which file the error occured

    # Combine all extracted data
    if extracted_data:
        #take all the extracted data

        organized_data = pd.concat(extracted_data, ignore_index=True)
        return organized_data
    else:
        print("No data extracted.")
        return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    directory_path = input("Enter the directory path containing Excel files: ")
    metrics_to_extract = ["temperature", "flow rate", "pressure"]  # Example fields

    # Extract data
    result_df = extract_data_from_excel(directory_path, metrics_to_extract)

    # Save organized data to a new Excel file
    if not result_df.empty:
        output_file = "organized_data.xlsx"
        result_df.to_excel(output_file, index=False)
        print(f"Data saved to {output_file}")

