import os
import json
import yaml
import time

# import omnigibson as og
import sys;sys.path.append("/shared/liushuai/OmniGibson/prompt_files")
# from robot_action import *
import parse_json
import otter_query as query
from imp import reload
import env_utils_gpt as eu 
import openai
from otter_request import otter_request,code_llamarequest
# from gpt_request import gpt_request
from gpt_request_azure import gpt_request
import argparse


def parse_args():
    description = "EVLM_gpt_process"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('idx', type=int, help='Index for data entry')
    return parser.parse_args()


def gpt_process(args):
    
    idx = args.idx
    with open('./EVLM_Task/val_21tasksmall.json') as f: #TODO change the path
        data = json.load(f)
    EVLM_name=sorted(list(data))[idx]
    # print(data[EVLM_name]['split'])

    if True:
        task_name=data[EVLM_name]['task_name']
        # detailed_name=data[EVLM_name]['detailed_name']
        # gpt_name=data[EVLM_name]['gpt_task']
        scene=data[EVLM_name]['env']
        print(idx)
        print(f"EVLM:{EVLM_name}")
        print(f"task_name:{task_name}")
        # print(f"detailed_name:{detailed_name}")
        task_data = data[EVLM_name]
        save_path = eu.f_mkdir(os.path.join('/shared/liushuai/OmniGibson/evaluation/data', EVLM_name))
        # main task loop
        
        main_task_flag = False
        subtask_iter = 1
        gpt_query = query.Query()
        for i in range(1, 7):
            eu.f_mkdir(os.path.join(save_path, f"subtask_{i}"))
        while True:

            # make the directory
            sub_save_path = eu.f_mkdir(os.path.join(save_path, f"subtask_{subtask_iter}"))
            
            # init pipeline for each subtask
            while True:
                with open("./evaluation/failed_task.json","r")as f:
                    data = json.load(f)
                    if EVLM_name in data.keys():
                        return 0
                if os.path.exists(os.path.join(sub_save_path, 'task1.json')): #TODO align with "task1"
                    break   
                time.sleep(1)
            while True:
                statinfo = os.stat(os.path.join(sub_save_path, 'task1.json')) 
                if statinfo.st_size > 0:
                    break
            human_info = parse_json.parse_json(path=os.path.join(sub_save_path, "task1.json"))
            
            with open("./evaluation/failed_task.json","r")as f:
                data = json.load(f)
                if EVLM_name in data.keys():
                    return 0
            
            # subtask loop, when a subtask is finished, close the loop
            while True:
                system_message = gpt_query.render_system_message()
                human_message = gpt_query.render_otter_message(
                    scene_graph=human_info[0], object=human_info[1],
                    inventory=human_info[2], task=human_info[3] 
                )
                all_messages = [system_message, human_message]
                content=human_message.content
                eu.save_input(sub_save_path, human_message.content)
                print("start query")
                succuss = True
                
                image_list = [os.path.join(sub_save_path, f'rgb{i}_detect_surroundings.png') for i in range(8)]
                for i in [os.path.join(sub_save_path, f'rgb{i}_BEV_surroundings.png') for i in range(8,10)]:
                    image_list.append(i)
                if True:
                    while succuss:
                        signal=True
                        for i in range(20):
                            try:
                                if i==20:
                                    return 0
                                print(f"try:{i}")
                                response=otter_request(content, image_list)
                                response=response.replace("\\n","\n")
                                answer = gpt_query.process_ai_message(sub_save_path,response,EVLM_name)
                                #if parsed succuessfully:
                                succuss = False
                                signal=True
                                break
                            except Exception as e:
                                answer = str(e)
                                print(answer)
                                succuss = False
                                signal=False
                            # except Exception as e:
                            #     print(f"Error: {e}")
                            #     if "exceeded" in str(e):
                            #         print("Sleeping for 3 seconds")
                            #         succuss = True
                            #         time.sleep(3)
                            #     else:
                            #         succuss = True
                            #         response = {"error_message": str(e)}
                            #         print(response)
                ##just for test:
                # with open("/shared/liushuai/OmniGibson/evaluation/1.txt",'r')as f:
                #     response=f.read()
                # try:
                #     response=response.replace("\\n","\n")
                #     answer = gpt_query.process_ai_message(sub_save_path,response,EVLM_name)
                # except Exception as e:
                #     answer = str(e)
                #     print(answer)
                    
                eu.save_response(sub_save_path, answer)
                if signal==False:
                    return 0

                while True:
                    with open("./evaluation/failed_task.json","r")as f:
                        data = json.load(f)
                        if EVLM_name in data.keys():
                            return 0               
                    if os.path.exists(os.path.join(sub_save_path, 'feedback.json')):
                        break
                    time.sleep(1)
                    
                while True:
                    feedbackinfo = os.stat(os.path.join(sub_save_path, 'feedback.json')) 
                    if feedbackinfo.st_size > 0:
                        break
                    
                with open("./evaluation/failed_task.json","r")as f:
                    data = json.load(f)
                    if EVLM_name in data.keys():
                        return 0

                with open(os.path.join(sub_save_path, 'feedback.json')) as f:
                    data = json.load(f) 
                
                main_task_flag = data['main_succeed']      
                if data['critic'] == 'succeed':
                    print('Task succeed!')
                    gpt_query.record_history(subtask=data['subtask'], code=data['code'], error='')

                    break
                else:

                    if data['reset']:
                        gpt_query.record_history(subtask=answer['subtask'], code=answer['code'], error='')
                        break
                    else:
                        gpt_query.record_history(subtask=answer['subtask'], code=answer['code'], error='')
                        break
            

            
            # reset parameters
            subtask_iter += 1
            
            #write json
            if subtask_iter>6:
                print(f"already attempt {subtask_iter} time, it is too long!")
                return 0

            if main_task_flag:    
                return 0


if __name__ == "__main__":
    args = parse_args()
    gpt_process(args)