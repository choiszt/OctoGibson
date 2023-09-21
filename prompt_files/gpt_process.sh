#!/bin/bash

# The number of data entries in your Python script
NUM_ENTRIES=72
# Loop through each index and run the Python script
for ((i=36; i<$NUM_ENTRIES; i++))
do
    python prompt_files/execute_gpt_no_args_json.py $i > prompt_files/log_data/gpt_$i.txt 2>&1
done