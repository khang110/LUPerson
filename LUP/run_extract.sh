#!/bin/bash

# Shell script to run download.py with a dynamic part number

# Default part number
PART_NUM=${1:-1}

# Set variables for arguments
VIDEO_DIR="videos/part_${PART_NUM}"
SAVE_DIR="luperson/part_${PART_NUM}"

# Check if the Python script exists
if [ ! -f "extract.py" ]; then
    echo "Error: extract.py not found!"
    exit 1
fi

# Run the Python script with the specified arguments
python3 extract.py -v "$VIDEO_DIR" -d dets -s "$SAVE_DIR"