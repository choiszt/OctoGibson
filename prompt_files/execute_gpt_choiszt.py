import os
import json
import yaml

# import omnigibson as og

# from robot_action import *
import parse_json
import query
from imp import reload
import env_utils_gpt as eu 
import openai
import re

def gpt_process(save_path, openai_api_key):
    # main task loop
    
    main_task_flag = False
    subtask_iter = 1
    gpt_query = query.Query(openai_api_key=openai_api_key)
    while True:
        
        # make the directory
        sub_save_path = eu.f_mkdir(os.path.join(save_path, f"subtask_{subtask_iter}"))
        
        # init pipeline for each subtask
        while True:
            if os.path.exists(os.path.join(sub_save_path, 'task1.json')): #TODO align with "task1"
                break   
        while True:
            statinfo = os.stat(os.path.join(sub_save_path, 'task1.json')) 
            if statinfo.st_size > 0:
                break
        
        
        # subtask loop, when a subtask is finished, close the loop
        while True:
            response_info = os.stat("/shared/liushuai/OmniGibson/prompt_files/gpt_response_choiszt.json") 
            if response_info.st_size > 0:
                break
        while True:
            with open("/shared/liushuai/OmniGibson/prompt_files/gpt_response_choiszt.json","r")as f:
                response=json.load(f)
            
            try:
                answer=response
            except Exception as e:
                answer = str(e)
                print(answer)
            eu.save_response(sub_save_path, answer)
            
            while True:
                if os.path.exists(os.path.join(sub_save_path, 'feedback.json')):
                    break
            while True:
                feedbackinfo = os.stat(os.path.join(sub_save_path, 'feedback.json')) 
                if feedbackinfo.st_size > 0:
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

api_key="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"
gpt_process(save_path="/shared/liushuai/OmniGibson/prompt_files/data",openai_api_key=api_key)