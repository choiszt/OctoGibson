import os
import json
from parse_annotation import *
import env_utils_sim as eu 
from run_command_no_args import *

TASK_NUM = 100
base_path = './data'
    
for i in range(TASK_NUM):    
    
    ### run command

    test1_command = "python prompt_files/execute_gpt.py"
    test2_command = "python prompt_files/execute_sim.py --/log/level=error --/log/fileLogLevel=error --/log/outputStreamLevel=error"
    conda_env1 = "gpt"
    conda_env2 = "omni"
    processes = []
    processes.append(run_command_in_terminal(test1_command, conda_env1))
    processes.append(run_command_in_terminal(test2_command, conda_env2))
    
    check_processes(processes)