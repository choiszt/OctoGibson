#!/bin/bash

# The number of data entries in your Python script
NUM_ENTRIES=26

# Loop through each index and run the Python script
for ((i=25; i<$NUM_ENTRIES; i++))
do
    python prompt_files/for_jingkang/load_scene_get_name.py $i --/log/level=error --/log/fileLogLevel=error --/log/outputStreamLevel=error > prompt_files/for_jingkang/log_0829/$i.txt 2>&1
done
