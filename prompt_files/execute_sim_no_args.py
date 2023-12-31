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
from verify_taskgoal import verify_taskgoal
import argparse

# def parse_args():
#     description = "EVLM_sim_process"
#     parser = argparse.ArgumentParser(description=description)
#     parser.add_argument("-t", "--task_name", type=str, help="task name to get bddl", required=True)
#     parser.add_argument("-g", "--gpt_task_name", type=str, help="task name for gpt", required=True)
#     parser.add_argument("-s", "--scene_name", type=str, help="scene name to get bddl", required=True)
#     parser.add_argument("-a", "--action_path", type=str, help="action path", required=True)
#     parser.add_argument("-r", "--removed_items", type=str, help="removed items for bddl", required=True)
#     parser.add_argument("-target", "--target_states", type=str, help="main task target states", required=True)
#     parser.add_argument("-save", "--save_path", type=str, help="data save path", required=True)
#     parser.add_argument("-l", "--/log/level", type=str, help="error log 1", required=True)
#     parser.add_argument("-f", "--/log/fileLogLevel", type=str, help="error log 2", required=True)
#     parser.add_argument("-o", "--/log/outputStreamLevel", type=str, help="error log 3", required=True)
#     return parser.parse_args()


def sim_process(args): #(a,b),(a,b,c)
    # task_name = args.task_name
    # gpt_task_name = args.gpt_task_name
    # scene_name = args.scene_name
    # action_path = args.action_path
    # save_path = args.save_path
    # main_target_states = args.target_states
    # removed_items = args.removed_items

    try:

        heading="import os \nimport json\nimport yaml\nimport omnigibson as og\nfrom action_list import * \nfrom action_utils import *\n"
        config_filename="./prompt_files/bddl_task.yaml"
        cfg = yaml.load(open(config_filename, "r"), Loader=yaml.FullLoader)

        task_we_have=os.listdir("/Users/liushuai/Desktop/omnigibson-master/prompt_files/data")
        now_task=sorted(task_we_have)[-1]


        #TODO read json after activate the env
        with open("/Users/liushuai/Desktop/omnigibson-master/EVLM_Task/task_0908.json" ,"r")as f:
            task_json=json.load(f)
        # sorted_task_list=sorted(list(task_json.keys()))


        # now_gpt_task=str(set(loaded_task)-set(loaded_task_copy))
        # now_task=task_json[now_gpt_task]
        # for ele in task_json.keys():
        #     if ele not in loaded_task:
        #         loaded_task.append(ele)
        #         now_task=task_json[ele]
        #         break
        task_name=now_task['task_name']
        gpt_task_name=now_task['gpt_task']
        scene_name=now_task['env']
        main_target_states=now_task['target_states']
        removed_items=now_task["removed_item"]

        cfg["task"]["online_object_sampling"] = False
        cfg["scene"]["scene_model"] =scene_name
        cfg["task"]["activity_name"] = task_name
        print(cfg)

        # Load the environment
        env = og.Environment(configs=cfg, action_timestep=1/60., physics_timestep=1/60.)

        # task_path=f"./prompt_files/data/{gpt_task_name}"
        # action_path = os.path.join(save_path, 'action.py')
        robot = env.robots[0]
        camera= og.sim.viewer_camera 
        bbox_modalities =["bbox_2d_loose"]# "bbox_2d_tight" not use 
        for bbox_modality in bbox_modalities:
            camera.add_modality(bbox_modality)
        camera.focal_length = 10.
        
        # main task loop
        subtask_iter = 1
        while True:     

            main_succeed = False
            
            while True:
                if os.path.exists(os.path.join(save_path, f"subtask_{subtask_iter}")):
                    break
            sub_save_path = os.path.join(save_path, f"subtask_{subtask_iter}")
            init_pipeline(env, robot, camera,task_name=str(gpt_task_name), file_name=sub_save_path, removed_items=removed_items)
            response_path = os.path.join(sub_save_path, 'response.json')
            feedback_path = os.path.join(sub_save_path, 'feedback.json')
            
            #subtask loop
            while True:  
                reset = False
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
                    with open(f"/shared/liushuai/OmniGibson/prompt_files/data/{gpt_task_name}/subtask_{subtask_iter}/action.py", 'w') as f:
                        f.write(heading)
                        f.write(code)
                    # time.sleep(2)
                    sys.path=list(set(sys.path))
                    if(subtask_iter!=1):
                        sys.path.remove(f"/shared/liushuai/OmniGibson/prompt_files/data/{gpt_task_name}/subtask_{subtask_iter-1}")
                    sys.path.append(f"/shared/liushuai/OmniGibson/prompt_files/data/{gpt_task_name}/subtask_{subtask_iter}")
                    import action
                    time.sleep(1)
                    try:
                        reload(action)
                        time.sleep(2)
                        action.act(robot,env,camera)
                        print("act...")
                    except Exception as e:
                        error = str(e)
                        env.reset()
                        robot.inventory=[]
                        robot.visible_only=True
                        subtask = subtask
                        code = code
                        error = error
                        critic = 'fail'
                        reset = True
                        break
                
                # subtask verification
                target_states = answer
                # verify function
                #comment the verification of inventory
                # if target_states['inventory'] != 'None': #TODO string None
                #     value = eu.verify_inv(env, robot, target_states['inventory'])
                #     print(f"target_inv:{target_states['inventory']}")
                #     print(f"inventory:{robot.inventory}")
                #     if not value: #TODO need to fix the bug
                #         error += f"{target_states['inventory']} is not in Inventory.\n"
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
                    env.reset()
                    robot.inventory=[]
                    break

            # reset parameters

            ###reset and run the previous code #TODO: NEED TO DELETE subtask_iter python.py *** CHOISZT 8.28
            
            # for iter_num in range(1,subtask_iter):
            #     path=f"/shared/liushuai/OmniGibson/prompt_files/data/{gpt_task_name}/subtask_{iter_num}"
            #     with open(os.path.join(path,"feedback.json"))as f:
            #         tmp_feedback=json.load(f)
            #     if tmp_feedback['critic']=='succeed':
            #         sys.path.append(path)
            #         import action
            #         action.act(robot,env,camera)

            subtask_iter += 1
            #TODO choiszt need to add renametarget_states
            #verify the whole task
            if critic == 'succeed':
                signal=False
                target=main_target_states
                for tar in target:
                    if not verify_taskgoal(env,*tar):
                        signal=False
                        break
                    signal=True
                if signal:
                    main_succeed = True
                    print(f"finish {gpt_task_name}!!!!! congrats!!!!!")
                    eu.save_feedback(feedback_path, subtask, code, error, critic, reset, main_succeed)
                    break
                else:
                    eu.save_feedback(feedback_path, subtask, code, error, critic, reset, main_succeed)
            else:
                eu.save_feedback(feedback_path, subtask, code, error, critic, reset, main_succeed)
            
            if reset: #
                if subtask_iter!=1:
                    for iter_num in range(1,subtask_iter):
                        path=f"./prompt_files/data/{gpt_task_name}/subtask_{iter_num}"
                        with open(os.path.join(path,"feedback.json"))as f:
                            tmp_feedback=json.load(f)
                        if tmp_feedback['critic']=='succeed':
                            time.sleep(1)
                            module=importlib.import_module(f"prompt_files.data.{gpt_task_name}.subtask_{iter_num}.action")
                            print(f"prompt_files.data.{gpt_task_name}.subtask_{iter_num}.action retrieve")
                            module.act(robot,env,camera)   
            if subtask_iter>15:
                print(f"already attempt {subtask_iter} time, it is too long!")
                break
        return 0
                        
    except:
        raise Exception
if __name__ == "__main__":
    args = parse_args()
    sim_process(args)