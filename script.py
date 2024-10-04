#!/usr/bin/env python3

import os
import shutil
import conda.cli.python_api as Conda
import csv
import subprocess

import pandas as pd


#install req packages:
subprocess.check_call([sys.executable, '-r', 'pip', 'install', 'requirements.txt'])



inp = input('Please provide the name of the csv with the data(dont include the .csv)')
# run data analysis each time writting to a file
df = pd.read_csv(inp+'.csv')



#transmit the data



#delete the file that the data was written to
os.remove("")