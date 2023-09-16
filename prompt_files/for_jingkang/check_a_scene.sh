#!/bin/bash

# The number of data entries in your Python script
NUM_ENTRIES=34

# Loop through each index and run the Python script
for ((i=0; i<$NUM_ENTRIES; i++))
do
    python check_a_scene.py $i > log_0829/$i.txt 2>&1
done
