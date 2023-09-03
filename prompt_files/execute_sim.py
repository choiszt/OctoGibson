import os
import json
import yaml

import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.ui_utils import choose_from_options

from robot_action import *
# import prompt_files.action as action
from importlib import reload
import importlib
import env_utils_sim as eu 
from initial_pipeline import *
import time
from bddl_verification import *
import sys
import bddl
import verify_taskgoal
def sim_process(task_name, scene_name, action_path, save_path):
    heading="import os \nimport json\nimport yaml\nimport omnigibson as og\nfrom action_list import * \nfrom action_utils import *\n"
    config_filename="./prompt_files/bddl_task.yaml"
    cfg = yaml.load(open(config_filename, "r"), Loader=yaml.FullLoader)
    cfg["task"]["online_object_sampling"] = False
    cfg["scene"]["scene_mdoel"] = scene_name
    cfg["task"]["activity_name"] = task_name
    # Load the environment
    env = og.Environment(configs=cfg, action_timestep=1/60., physics_timestep=1/60.)

    robot = env.robots[0]
    camera= og.sim.viewer_camera 
    bbox_modalities =["bbox_2d_loose"]# "bbox_2d_tight" not use 
    for bbox_modality in bbox_modalities:
        camera.add_modality(bbox_modality)
    camera.focal_length = 10.
    
    # main task loop
    subtask_iter = 1
    # while True:
    #     if subtask_iter!=1:
    #         for iter_num in range(1,subtask_iter):
    #             path=f"/shared/liushuai/OmniGibson/prompt_files/data/{task_name}/subtask_{iter_num}"
    #             with open(os.path.join(path,"feedback.json"))as f:
    #                 tmp_feedback=json.load(f)
    #             if tmp_feedback['critic']=='succeed':
    #                 time.sleep(1)
    #                 module=importlib.import_module(f"prompt_files.data.{task_name}.subtask_{iter_num}.action")
    #                 time.sleep(1)
    #                 module.act(robot,env,camera)        

        main_succeed = False
        
        while True:
            if os.path.exists(os.path.join(save_path, f"subtask_{subtask_iter}")):
                break
        sub_save_path = os.path.join(save_path, f"subtask_{subtask_iter}")
        init_pipeline(env, robot, camera,task_name=str(task_name), file_name=sub_save_path)
        response_path = os.path.join(sub_save_path, 'response.json')
        feedback_path = os.path.join(sub_save_path, 'feedback.json')
        
        #subtask loop
        while True:  
            error=''
            # wait for the GPT response
            while True:
                if os.path.exists(response_path):
                    break
            while True:
                response_info = os.stat(response_path) 
                if response_info.st_size > 0:
                    break
            with open(response_path) as f:
                data = json.load(f)
            answer = data['response']
            if isinstance(answer, str):
                subtask = ""
                code = ""
                error = answer
                critic = 'fail'
                reset = False
                break
            else:
                subtask, code = answer['subtask'], answer['code']
                with open(f"/shared/liushuai/OmniGibson/prompt_files/data/{task_name}/subtask_{subtask_iter}/action.py", 'w') as f:
                    f.write(heading)
                    f.write(code)
                # time.sleep(2)
                sys.path=list(set(sys.path))
                if(subtask_iter!=1):
                    sys.path.remove(f"/shared/liushuai/OmniGibson/prompt_files/data/{task_name}/subtask_{subtask_iter-1}")
                sys.path.append(f"/shared/liushuai/OmniGibson/prompt_files/data/{task_name}/subtask_{subtask_iter}")
                import action
                time.sleep(1)
                try:
                    reload(action)
                    time.sleep(2)
                    action.act(robot,env,camera)
                    print("act...")
                except Exception as e:
                    error = str(e)
                    # env.reset()
                    robot.inventory=[]
                    subtask = subtask
                    code = code
                    error = error
                    critic = 'fail'
                    reset = True
                    break
            
            # subtask verification
            target_states = answer
            # verify function
            if target_states['inventory'] != 'None': #TODO string None
                value = eu.verify_inv(env, robot, target_states['inventory'])
                print(f"target_inv:{target_states['inventory']}")
                print(f"inventory:{robot.inventory}")
                if not value: #TODO need to fix the bug
                    error += f"{target_states['inventory']} is not in Inventory.\n"
            for obj in target_states['obj_2']:
                value = eu.verify_obj_2(env,obj[0], obj[1], obj[2])
                if not value:
                    error += f"State {obj[1]} of object {obj[0]} is not {obj[2]}\n"
            # for obj in target_states['obj_3']:
            #     value = eu.verify_obj_3(env,obj[0], obj[1], obj[2],obj[3])
            #     if not value:
            #         error += f"{obj[0]} is not {obj[1]} {obj[2]}\n"
            if len(error) == 0:
                subtask = subtask
                error = error
                critic = 'succeed'
                reset = False
                break
            else:
                subtask = subtask
                error = error
                critic = 'fail'
                reset = True
                # env.reset()
                break

        # reset parameters

        ###reset and run the previous code #TODO: NEED TO DELETE subtask_iter python.py *** CHOISZT 8.28
        
        # for iter_num in range(1,subtask_iter):
        #     path=f"/shared/liushuai/OmniGibson/prompt_files/data/{task_name}/subtask_{iter_num}"
        #     with open(os.path.join(path,"feedback.json"))as f:
        #         tmp_feedback=json.load(f)
        #     if tmp_feedback['critic']=='succeed':
        #         sys.path.append(path)
        #         import action
        #         action.act(robot,env,camera)

        subtask_iter += 1
        #TODO choiszt need to add rename
        #verify the whole task
        if critic == 'succeed':
            # signal = verify_taskgoal() 
            signal=False
            if signal:
                main_succeed = True
                eu.save_feedback(feedback_path, subtask, code, error, critic, reset, main_succeed)
                break
            else:
                eu.save_feedback(feedback_path, subtask, code, error, critic, reset, main_succeed)
        else:
            eu.save_feedback(feedback_path, subtask, code, error, critic, reset, main_succeed)


sim_process(task_name="cook_a_brisket",scene_name="Beechwood_0_int",action_path="./prompt_files/action.py",save_path="./prompt_files/data/cook_a_brisket")
