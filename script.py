import pandas as pd
import sys

def analyze_data(df, text_file_path):
    shape = df.shape
    data_types = df.dtypes
    missing_values = df.isnull().sum()
    summary_statistics = df.describe(include='all')

    with open(text_file_path, 'w') as text_file:
        text_file.write(f"Dataset Shape (rows, columns): {shape}\n")

        text_file.write("\nColumn Names and Data Types:\n")
        for col, dtype in data_types.items():
            text_file.write(f"{col}: {dtype}\n")
        
        text_file.write("\nMissing Values per Column:\n")
        for col, missing in missing_values.items():
            text_file.write(f"{col}: {missing}\n")

        text_file.write("\nSummary Statistics:\n")
        text_file.write(summary_statistics.to_string())
        
    return text_file_path

def load_dataset(file_base_name):
    file_path = file_base_name + '.csv'  # Add the .csv extension
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

if __name__ == "__main__":
    # Get the input and output file names from command-line arguments
    input_base_name = sys.argv[1]
    output_file = sys.argv[2]

    # Load the dataset and analyze data
    df = load_dataset(input_base_name)
    if df is not None:
        analyze_data(df, output_file)
