#!/bin/bash

# Shell script to run download.py with a dynamic part number

# Default part number
PART_NUM=${1:-1}

# Set variables for arguments
VID_NAME_FILE="split_vnames/part_${PART_NUM}/vnames.txt"
SAVE_DIR="videos/part_${PART_NUM}"

# Check if the Python script exists
if [ ! -f "download.py" ]; then
    echo "Error: download.py not found!"
    exit 1
fi

# Check if the video name file exists
if [ ! -f "$VID_NAME_FILE" ]; then
    echo "Error: Video name file $VID_NAME_FILE not found!"
    exit 1
fi

# Run the Python script with the specified arguments
python3 download.py -f "$VID_NAME_FILE" -s "$SAVE_DIR"
