#!/bin/bash
#!/bin/bash

# Variables
PYTHON_SCRIPT="script.py"  
REMOTE_USER="clbp"                       
REMOTE_HOST="birg.dev"                   
REMOTE_PATH_TO_BIRG="BIRG_CLBP_DATA_SCRIPT" # path to save output on remote server

# Prompt for necessary paths and input
echo "Enter the local path to the current directory (where your script and input file are located):"
read LOCAL_PATH

echo "Enter the path to the SSH private key file:"
read REMOTE_PATH_TO_SSHKEY

echo "Enter the full path to the directory of the input CSV file:"
read LOCAL_INPUT_PATH


echo "Enter the  name of the input CSV file:"
read INPUT_NAME

# Full paths for script and output
LOCAL_SCRIPT_PATH="$LOCAL_PATH/$PYTHON_SCRIPT"
LOCAL_OUTPUT_PATH="$LOCAL_PATH/$OUTPUT_FILE"


OUTPUT_FILE="$INPUT_NAME""_data.txt"     # name of the output text file

# Run the Python script with the input and output file names as arguments
python3 "$LOCAL_SCRIPT_PATH" "$LOCAL_INPUT_PATH/$INPUT_NAME" "$LOCAL_OUTPUT_PATH"

# Check if Python script ran successfully
if [ $? -eq 0 ]; then
    echo "Python script ran successfully. Output saved to $OUTPUT_FILE."

    # Copy the output text file to the remote server
    scp -i "$REMOTE_PATH_TO_SSHKEY" "$LOCAL_OUTPUT_PATH" "$REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH_TO_BIRG/$OUTPUT_FILE"

    # Check if scp was successful
    if [ $? -eq 0 ]; then
        echo "File successfully copied to $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH_TO_BIRG."
    else
        echo "Error: Failed to copy the file to the remote server."
    fi
else
    echo "Error: Python script did not run successfully."
fi

