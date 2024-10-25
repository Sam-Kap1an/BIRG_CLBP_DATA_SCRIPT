#!/bin/bash

# Variables
PYTHON_SCRIPT="script.py"  
INPUT_FILE="CLBP_test_csv"              #  name for the input file w/o .csv extension
OUTPUT_FILE="CLBP_test_csv_data.txt"        # name of the output text file
REMOTE_USER="clbp"              
REMOTE_HOST="birg.dev"     
REMOTE_PATH="~/BIRG_CLBP_DATA_SCRIPT"      

# Run the Python script with the input and output file names as arguments
python3 "$PYTHON_SCRIPT" "$INPUT_FILE" "$OUTPUT_FILE"

# Check if Python script ran successfully
if [ $? -eq 0 ]; then
    echo "Python script ran successfully. Output saved to $OUTPUT_FILE."

    # Copy the text file to the remote server
    scp "$OUTPUT_FILE" "$REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH"

    # Check if scp was successful
    if [ $? -eq 0 ]; then
        echo "File successfully copied to $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH."
    else
        echo "Error: Failed to copy the file to the remote server."
    fi
else
    echo "Error: Python script did not run successfully."
fi
