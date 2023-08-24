import os
import json
import yaml

import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.ui_utils import choose_from_options

from robot_action import *
import action
import parse_json
import query
from imp import reload
import env_utils as eu 
from initial_pipeline import *

from bddl_verification import *

def gpt_process(save_path, openai_api_key):
    # main task loop
    
    main_task_flag = False
    subtask_iter = 1
    while True:
        
        # make the directory
        sub_save_path = eu.f_mkdir(os.path.join(save_path, f"subtask_{subtask_iter}"))
        
        # init pipeline for each subtask
        while True:
            if os.path.exists(os.path.join(sub_save_path, 'task.json')):
                break        
        human_info = parse_json.parse_json(path=os.path.join(sub_save_path, "task.json"))
        gpt_query = query.Query(openai_api_key=openai_api_key)
        
        # subtask loop, when a subtask is finished, close the loop
        while True:
            system_message = gpt_query.render_system_message()
            human_message = gpt_query.render_human_message(
                scene_graph=human_info[0], object=human_info[1],
                inventory=human_info[2], task=human_info[3] 
            )
            all_messages = [system_message, human_message]
            
            eu.save_input(sub_save_path, human_message.content)

            response = gpt_query.llm(all_messages)
            answer = gpt_query.process_ai_message(response)
            
            eu.save_response(sub_save_path, answer)
            
            while True:
                if os.path.exists(os.path.join(sub_save_path, 'feedback.json')):
                    break
            
            with open(os.path.join(sub_save_path, 'feedback.json')) as f:
                data = json.load(f) 
            
            main_task_flag = data['main_succeed']      
            if data['critic'] == 'succeed':
                print('Task succeed!')
                gpt_query.record_history(subtask=data['subtask'], code=data['code'], error=data['error'])
                break
            else:
                if data['reset']:
                    gpt_query.record_history(subtask=answer['subtask'], code=answer['code'], error=data['error'])
                    break
                else:
                    gpt_query.record_history(subtask=answer['subtask'], code=answer['code'], error=data['error'])
                    break

        # reset parameters
        subtask_iter += 1
        
        if main_task_flag:
            break