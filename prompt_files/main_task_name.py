import os
import json
from parse_annotation import *
import env_utils_sim as eu 
from run_command_task_name import *

TASK_NUM = 100
base_path = './data'
with open('./excel.json') as f:
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
    conda_env2 = "omni"
    processes = []
    processes.append(run_command_in_terminal(command_args1, 'gpt', conda_env1))
    processes.append(run_command_in_terminal(command_args2, 'omni', conda_env2))
    
    check_processes(processes)