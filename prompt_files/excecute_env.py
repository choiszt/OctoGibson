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

# Make sure object states are enabled
gm.ENABLE_OBJECT_STATES = True


def exec(task_name=None, scene_name=None, 
         save_path=None, action_path=None,
         openai_api_key=None):
    '''
    task_name: name of the task
    scene_name: name of the loaded scene
    json_path: path to save the json files of data collection in init pipeline
    save_path: path to save the collected training data
    action_path: path to write the repsonse code
    openai_api_key: api key for GPT4
    '''
    
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
    retry = 1
    while True:
        
        # make the directory
        sub_save_path = eu.f_mkdir(os.path.join(save_path, f"subtask_{subtask_iter}"))
        
        # init pipeline for each subtask
        # TODO: need to restore each json file for each subtask, use subtask_iter to create the name of json file. @choizst
        
        init_pipeline(env, robot, camera,task_name=str(task_name), file_name=sub_save_path)  
        human_info = parse_json.parse_json(path=os.path.join(sub_save_path, "task.json"))
        gpt_query = query.Query(openai_api_key=openai_api_key)
        
        # subtask loop, when a subtask is finished, close the loop
        while True:
            retry_data_path = eu.f_mkdir(os.path.join(sub_save_path, f"retry_{retry}"))
            system_message = gpt_query.render_system_message()
            human_message = gpt_query.render_human_message(
                scene_graph=human_info[0], object=human_info[1],
                inventory=human_info[2], task=human_info[3] 
            )
            all_messages = [system_message, human_message]
            
            eu.save_input(retry_data_path, human_message.content)

            response = gpt_query.llm(all_messages)
            answer = gpt_query.process_ai_message(response)

            error = ""       
            if isinstance(answer, str):
                error = answer
                gpt_query.record_history(error=error)
                eu.save_response(retry_data_path, answer, error)
                retry += 1
                continue
            else:
                exec_code = answer['code']
                with open(action_path, 'w') as f:
                    f.write(exec_code)
                reload(action)
                try:
                    action.act(robot, env, camera)
                except Exception as e:
                    error = str(e)
                    gpt_query.record_history(subtask=answer['subtask'], code=answer['code'], error=error)
                    eu.save_response(retry_data_path, answer, error)
                    retry += 1
                    env.reset()
                    break
            
            target_states = answer['target']

            # verify function
            if target_states['inv'] is not None:
                value = eu.verify_inv(env, robot, target_states['inv'])
                if not value:
                    error += f"\n{target_states['inv']} is not in Inventory.\n"
            for obj in target_states['obj_2']:
                value = eu.verify_obj_2(obj[0], obj[1], obj[2])
                if not value:
                    error += f"\nState {obj[1]} of object {obj[0]} is not {obj[2]}\n"
            
            ### TODO: add function for binary states
            # for obj in target_states['obj_3']:
            #     value = u.verify_obj_3(obj[0], obj[1], obj[2], obj[3])
            #     if not value:
            #         error += f"State {obj[1]} between {obj[0]} and {obj[2]} is not {obj[3]}"
            
            if len(error) == 0:
                print('Task succeed!')
                gpt_query.record_history(subtask=answer['subtask'], code=answer['code'], error=error)
                eu.save_response(retry_data_path, answer, error)
                break
            else:
                gpt_query.record_history(subtask=answer['subtask'], code=answer['code'], error=error)
                eu.save_response(retry_data_path, answer, error)
                retry += 1
                env.reset()
                break

        # reset parameters
        retry = 1
        subtask_iter += 1
        
        #verify the whole task
        signal = verify_bddl()
        if signal:
            break
        

if __name__ == "__main__":
    exec(task_name="cook_bacon",scene_name="Merom_1_int",save_path="/shared/liushuai/OmniGibson/prompt_files/trash")
