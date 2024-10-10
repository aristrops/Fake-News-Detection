import pandas as pd
import sys

"""
Used to extract the necessary columns from a csv file.
"""
def extract_columns(input_csv, output_csv, columns, sample_size=None):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_csv)

    # Check if the specified columns exist in the DataFrame
    for column in columns:
        if column not in df.columns:
            raise ValueError(f"Column '{column}' not found in the input CSV file.")
    
    # Select the specified columns
    selected_columns_df = df[columns]
    
    # If a sample size is specified, take a sample from the DataFrame
    if sample_size:
        selected_columns_df = selected_columns_df.sample(n=sample_size)
    
    # Save the selected columns to a new CSV file
    selected_columns_df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python extract_columns.py <input_csv> <output_csv> <columns> [sample_size]")
    else:
        input_csv = sys.argv[1]
        output_csv = sys.argv[2]
        columns = sys.argv[3].split(',')  # Split the columns by comma
        sample_size = int(sys.argv[4]) if len(sys.argv) == 5 else None
        extract_columns(input_csv, output_csv, columns, sample_size)
