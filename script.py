#!/usr/bin/env python3

import os
import shutil
import conda.cli.python_api as Conda
import csv
import subprocess
import pandas as pd
import socket

#install req packages:
subprocess.check_call([sys.executable, '-r', 'pip', 'install', 'requirements.txt'])


inp = input('Please provide the name of the csv with the data(dont include the .csv)')
text_file_path = inp + '_data.txt'

# run data analysis each time writting to a file
df = pd.read_csv(inp+'.csv')



#transmit the data using sockets
def transmit_file(file_path):
    HOST, PORT = 'localhost', #IP/port??
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # open text file and send contents
        with open(file_path, 'rb') as f:
            data = f.read()
            s.sendall(data)
    print(f'Transmitted {file_path}.')

transmit_file(text_file_path)

# dlete text file after transmit
if os.path.exists(text_file_path):
    os.remove(text_file_path)
    print(f'{text_file_path} deleted.')
else:
    print(f'{text_file_path} does not exist.')