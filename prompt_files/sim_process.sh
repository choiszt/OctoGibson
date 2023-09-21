#!/bin/bash

# The number of data entries in your Python script
NUM_ENTRIES=72
# Loop through each index and run the Python script
for ((i=36; i<$NUM_ENTRIES; i++))
do
    python prompt_files/execute_sim_no_args_json.py $i --/log/level=error --/log/fileLogLevel=error --/log/outputStreamLevel=error > prompt_files/log_data/sim_$i.txt 2>&1
done
