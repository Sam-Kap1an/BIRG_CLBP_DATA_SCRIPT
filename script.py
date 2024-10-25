import pandas as pd
import sys

def analyze_data(df, text_file_path):
    shape = df.shape
    column_names = df.columns.tolist()
    with open(text_file_path, 'w') as text_file:
        text_file.write(f"Dataset Shape (rows, columns): {shape}\n")
        text_file.write(f"\nColumn Names:\n{', '.join(column_names)}\n")

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
