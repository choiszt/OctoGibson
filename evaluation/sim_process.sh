#!/bin/bash

# The number of data entries in your Python script
NUM_ENTRIES=35
# Loop through each index and run the Python script
for ((i=24; i<$NUM_ENTRIES; i++))
do
    python evaluation/execute_sim_no_args_json.py $i --/log/level=error --/log/fileLogLevel=error --/log/outputStreamLevel=error > evaluation/log_data/sim_$i.txt 2>&1
done
