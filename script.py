import pandas as pd
import numpy as np
import sys

def analyze_data(df, text_file_path):
    with open(text_file_path, 'w') as text_file:
        dtype_df = df.applymap(lambda x: np.NaN if pd.isnull(x) else type(x).__name__)
        dtype_df.to_csv(text_file_path, index=False)
        
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
