#
# Rylee Leavitt
# 3/5/2025
# SDEV1100 1st project
# SDEV 1100
#
#data_Standardization.py
import os
import pandas as pd

# Define a function to standardize data
def standardize_data(df, column_mapping, date_columns=None, numeric_columns=None):
    """
    Standardizes the DataFrame by:
    - Renaming and reordering columns based on a consistent schema (column_mapping).
    - Formatting date columns to a standard format.
    - Rounding numerical columns to a consistent precision.

    Args:
        df (pd.DataFrame): Input DataFrame.
        column_mapping (dict): Mapping of original column names to standardized names.
        date_columns (list, optional): List of date column names to standardize.
        numeric_columns (dict, optional): Dict with column names and desired precision for numeric columns.

    Returns:
        pd.DataFrame: Standardized DataFrame.
    """
    # Map columns to standardized names
    df = df.rename(columns=column_mapping)
    df = df[column_mapping.values()]  # Reorder columns

    # Standardize date columns
    if date_columns:
        for col in date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime("%Y-%m-%d")

    # Standardize numeric columns
    if numeric_columns:
        for col, precision in numeric_columns.items():
            if col in df.columns:
                df[col] = df[col].round(precision)

    return df

# Function to extract and standardize data from multiple Excel files
def extract_and_standardize_data(directory, metrics, column_mapping, date_columns=None, numeric_columns=None):
    """
    Extracts data from Excel files in a directory and standardizes it.

    Args:
        directory (str): Path to the directory containing Excel files.
        metrics (list): List of original data fields to extract.
        column_mapping (dict): Mapping of original column names to standardized names.
        date_columns (list, optional): List of date column names to standardize.
        numeric_columns (dict, optional): Dict with column names and desired precision for numeric columns.

    Returns:
        pd.DataFrame: Aggregated and standardized data.
    """
    extracted_data = []

    for filename in os.listdir(directory):
        if filename.endswith(".xlsx") or filename.endswith(".xls"):
            filepath = os.path.join(directory, filename)
            try:
                df = pd.read_excel(filepath)
                # Filter relevant columns
                filtered_data = df[metrics]
                filtered_data["Source_File"] = filename
                # Standardize the extracted data
                standardized_data = standardize_data(
                    filtered_data, column_mapping, date_columns, numeric_columns
                )
                extracted_data.append(standardized_data)
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

    if extracted_data:
        return pd.concat(extracted_data, ignore_index=True)
    else:
        return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    directory_path = input("Enter the directory path containing Excel files: ")
    metrics_to_extract = ["temp", "flowrate", "pressure", "date_measured"]  # Example fields from raw files

    # Column mapping: Map raw column names to standardized ones
    column_mapping = {
        "temp": "Temperature",
        "flowrate": "Flow Rate",
        "pressure": "Pressure",
        "date_measured": "Measurement Date",
        "Source_File": "Source_File"  # Keeping source tracking consistent
    }

    # Standardize date formats and numerical precision
    date_columns_to_standardize = ["Measurement Date"]
    numeric_columns_precision = {"Temperature": 2, "Flow Rate": 1, "Pressure": 2}

    # Extract and standardize the data
    result_df = extract_and_standardize_data(
        directory_path, metrics_to_extract, column_mapping, 
        date_columns_to_standardize, numeric_columns_precision
    )

    # Save the standardized data to a new Excel file
    if not result_df.empty:
        output_file = "standardized_data.xlsx"
        result_df.to_excel(output_file, index=False)
        print(f"Standardized data saved to {output_file}")
