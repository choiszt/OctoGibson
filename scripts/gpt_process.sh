#!/bin/bash

# The number of data entries in your Python script
NUM_ENTRIES=90
# Loop through each index and run the Python script
for ((i=2; i<$NUM_ENTRIES; i++))
do
    python execute_gpt_no_args_json.py $i > log_data_rerunerror2/gpt_$i.txt 2>&1
done