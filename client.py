#!/usr/bin/env python3

import os

import sys
import subprocess

#install req packages:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

import requests
import pandas as pd



def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


def analyze_data(df):
    #tdb
    return 

def transmit_result(api_url, result):
    try:
        response = requests.post(api_url, json={'result': result},headers=headers)
        if response.status_code == 200:
            print("Result transmitted successfully")
        else:
            print(f"Failed to transmit result: {response.status_code}")
    except Exception as e:
        print(f"Error transmitting result: {e}")


if __name__ == "__main__":
    api_url = "http://<your_server_ip>:8000/api/result" # hardcode API
    headers = {'x-api-key': '440dc1aa436f397a6f07439e21f40b25'}  # API key sent in the headers
    data = {'result': 'test_result'}

    inp = input('Please provide the name of the csv with the data(dont include the .csv)')
    text_file_path = inp + '_data.txt' 
    df = load_dataset(text_file_path)
    if df is not None:
        result = analyze_data(df)
        transmit_result(api_url, result)

    # dlete text file after transmit
    if os.path.exists(text_file_path):
        os.remove(text_file_path)
        print(f'{text_file_path} deleted.')
    else:
        print(f'{text_file_path} does not exist.')