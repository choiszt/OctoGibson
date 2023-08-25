import os
import json
import yaml

import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.ui_utils import choose_from_options

from robot_action import *
import action
from imp import reload
import prompt_files.env_utils_gpt as eu 
from initial_pipeline import *

from bddl_verification import *

def sim_process(task_name, scene_name, action_path, save_path):
    heading="import os \nimport json\nimport yaml\nimport omnigibson as og\nfrom action_list import * \nfrom action_utils import *\n"
    config_filename="/shared/liushuai/OmniGibson/prompt_files/bddl_task.yaml"
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
    while True:
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
            # wait for the GPT response
            while True:
                if os.path.exists(response_path):
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
                with open(action_path, 'w') as f:
                    f.write(heading)
                    f.write(code)
                reload(action)
                try:
                    action.act(robot, env, camera)
                    print("act...")
                except Exception as e:
                    error = str(e)
                    env.reset()
                    subtask = subtask
                    code = code
                    error = error
                    critic = 'fail'
                    reset = True
                    break
            
            # subtask verification
            target_states = answer['target']
            # verify function
            if target_states['inv'] is not None:
                value = eu.verify_inv(env, robot, target_states['inv'])
                if not value:
                    error += f"{target_states['inv']} is not in Inventory.\n"
            for obj in target_states['obj_2']:
                value = eu.verify_obj_2(obj[0], obj[1], obj[2])
                if not value:
                    error += f"State {obj[1]} of object {obj[0]} is not {obj[2]}\n"

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
                break

        # reset parameters
        subtask_iter += 1
        
        #verify the whole task
        if critic == 'succeed':
            signal = verify_bddl()
            if signal:
                main_succeed = True
                eu.save_feedback(feedback_path, subtask, code, error, critic, reset, main_succeed)
                break
            else:
                eu.save_feedback(feedback_path, subtask, code, error, critic, reset, main_succeed)
        else:
            eu.save_feedback(feedback_path, subtask, code, error, critic, reset, main_succeed)


sim_process(task_name="cook_bacon",scene_name="Merom_1_int",action_path="./action.py",save_path="./data")
