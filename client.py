#!/usr/bin/env python3

import os

import sys
import subprocess
import time

#install req packages:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'setuptools'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

import requests
import pandas as pd

text_file = 'sample_data.txt'
csv_file = "CLBP_test_csv.csv"


def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


def analyze_data(df, text_file_path):
    shape = df.shape
    column_names = df.columns.tolist()
    with open(text_file_path, 'w') as text_file:
        text_file.write(f"Dataset Shape (rows, columns): {shape}\n")
        text_file.write(f"\nColumn Names:\n{', '.join(column_names)}\n")

    return text_file_path

def transmit_result(api_url, text_file_path):
    with open(text_file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(api_url, files=files,timeout=60)
        
        if response.status_code == 200:
            print("File transmitted successfully.")
        else:
            print(f"Error transmitting result: {response.text}")


if __name__ == "__main__":
    api_url = "http://-------/api/upload" # hardcode API
    headers = {'x-api-key': '-----------'}  # API key sent in the headers
    data = {'result': 'test_result'}
    

    inp = input('Please provide the name of the csv the data(dont include the .csv)')
    text_file_path = inp + '_data.txt'

    df = load_dataset(inp + '.csv')
    if df is not None:
        analyze_data(df, text_file_path)
        transmit_result(api_url, text_file_path)

    # dlete text file after transmit
    if os.path.exists(text_file_path):
        time.sleep(1)  # Wait for a second
        try:
            os.remove(text_file_path)
            print(f'{text_file_path} deleted.')
        except PermissionError:
            print(f'PermissionError: Could not delete {text_file_path}. It may still be in use.')
    else:
        print(f'{text_file_path} does not exist.')