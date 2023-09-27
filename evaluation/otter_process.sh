#!/bin/bash

# The number of data entries in your Python script
NUM_ENTRIES=35
# Loop through each index and run the Python script
for ((i=24; i<$NUM_ENTRIES; i++))
do
    python evaluation/execute_otter_no_args_json.py $i > evaluation/log_data/gpt_$i.txt 2>&1
done