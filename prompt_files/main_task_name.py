import os
import json
from parse_annotation import *
# import env_utils_sim as eu 
from run_command_task_name import *

TASK_NUM = 1
base_path = './data'
with open('/home/cooyes/Desktop/liushuai/omnigibson/EVLM_Task/task_0911.json') as f:
    data = json.load(f)
    all_keys = list(data.keys())
    
for i in range(TASK_NUM):
    main_task_name = all_keys[i]
    
    
    ### run command
    command_args1 = {}
    command_args2 = {}
    command_args1['t'] = main_task_name
    command_args2['t'] = main_task_name
    

    conda_env1 = "gpt"
    conda_env2 = "omnigibson"
    processes = []
    processes.append(run_command_in_terminal(command_args1, 'gpt', conda_env1))
    processes.append(run_command_in_terminal(command_args2, 'omnigibson', conda_env2))
    print(main_task_name)
    
    # check_processes(processes)