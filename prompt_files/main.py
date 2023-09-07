import os
import json
from test_json import *
import env_utils_sim as eu 
from run_command import *

TASK_NUM = 100
base_path = './data'
for i in range(TASK_NUM):
    data = parse(i)
    task_name = data['bddl']
    scene_name = data['scene']
    gpt_name = data['gpt']
    removed_item = data['removed']
    target_states = data['target_states']
    
    save_path = eu.f_mkdir(os.path.join(base_path, gpt_name))
    action_path = os.path.join(save_path, 'action.py')
    
    ### run command
    command_args1 = {}
    command_args2 = {}
    command_args1['t'] = task_name
    command_args1['s'] = scene_name
    command_args1['g'] = gpt_name
    command_args1['a'] = action_path
    command_args1['r'] = removed_item
    command_args1['target'] = target_states
    command_args1['save'] = save_path
    command_args2['save'] = save_path
    
    run_command_in_terminal(command_args2, process_name='gpt', conda_env='gpt')
    run_command_in_terminal(command_args1, process_name='sim' conda_env='omni')