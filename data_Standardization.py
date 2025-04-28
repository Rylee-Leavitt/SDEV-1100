#
# Rylee Leavitt
# 3/5/2025
# SDEV1100 1st project
# SDEV 1100
#

#data_Standardization.py

import pandas as pd #imports the pandas library with the alias pd
from data_Extraction import extract_data #imports from the data_Extraction.py file
import os #imports the os module

def standardize_data(df):
    # Rename columns to a consistent format
    column_mapping = {
        "dtemperature": "Temperature",
        "flow rate": "FlowRate",
        "pressure": "Pressure",
    }
    df.rename(columns=column_mapping, inplace=True)

    # Ensure all columns are in a consistent order
    desired_columns = ["Temperature", "FlowRate", "Pressure"]
    for column in desired_columns:
        if column not in df.columns:
            df[column] = None  # Add missing columns
    df = df[desired_columns]  # Reorder columns
    return df

def consolidate_data(new_data, output_csv):
    # Check if the CSV file already exists
    if os.path.exists(output_csv):
        # Append new data to the existing file
        existing_data = pd.read_csv(output_csv)
        consolidated_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        # Create a new CSV file with new data
        consolidated_data = new_data

    # Save the consolidated data back to the CSV file
    consolidated_data.to_csv(output_csv, index=False)

def main():
    # Extract data using the extract_data function from data_Extraction.py
    extracted_data = extract_data()  # Modify this based on the actual function signature

    # Standardize the data
    standardized_data = standardize_data(extracted_data)

    # Consolidate the data into a single CSV file
    output_csv = "consolidated_data.csv"
    consolidate_data(standardized_data, output_csv)

if __name__ == "__main__":
    main()