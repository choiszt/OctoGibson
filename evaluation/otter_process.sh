#!/bin/bash

# The number of data entries in your Python script
NUM_ENTRIES=21
# PID variable to store the process ID
PID=0

# Loop through each index and run the Python script
for ((i=0; i<$NUM_ENTRIES; i++))
do
    python evaluation/execute_otter_no_args_json.py $i > evaluation/log_data/gpt_$i.txt 2>&1 &
    PID=$!

    # Periodically check if sim_$(i+1).txt is generated before gpt_$i.txt has finished
    while kill -0 $PID 2>/dev/null; do
        echo "Checking sim process $PID"
        if [ -f "evaluation/log_data/sim_$(($i+1)).txt" ]; then
            # If sim_$(i+1).txt is generated, kill the otter process
            echo "Killing otter process $PID since sim_$(($i+1)).txt has been generated"
            kill -9 $PID
            break
        fi
        sleep 60  # wait for a short period before checking again
    done
done

# Wait for the last process to complete
wait $PID
