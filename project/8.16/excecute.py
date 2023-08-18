import os
import json
import yaml

import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.ui_utils import choose_from_options
import sys;sys.path.append("/shared/liushuai/OmniGibson/project")
from robot_action import *
import action
import parse_json
# import query
# from imp import reload
# import communicate.env_utils as u
from initial_pipeline import *

# Make sure object states are enabled
gm.ENABLE_OBJECT_STATES = True


def main(random_selection=False, headless=False, short_exec=False, task_name=None, scene_name=None, json_path=None, save_path=None, action_path=None):
    config_filename="/shared/liushuai/OmniGibson/project/bddl_demo.yaml"
    cfg = yaml.load(open(config_filename, "r"), Loader=yaml.FullLoader)
    cfg["task"]["online_object_sampling"] = False
    cfg["scene"]["scene_model"] = scene_name
    cfg["task"]["activity_name"] = task_name
    # Load the environment
    env = og.Environment(configs=cfg, action_timestep=1/60., physics_timestep=1/60.)

    robot = env.robots[0]
    camera= og.sim.viewer_camera 
    bbox_modalities = ["bbox_2d_loose"]# "bbox_2d_tight" "bbox_3d"not use 
    for bbox_modality in bbox_modalities:
        camera.add_modality(bbox_modality)
    camera.focal_length = 10.

    # init pipeline
    json_path=init_pipeline(env, robot, camera)
    
    human_info = parse_json.parse_json(path=json_path)

    gpt_query = query.Query()
    system_message = gpt_query.render_system_message()
    human_message = gpt_query.render_human_message(
        scene_graph=human_info[0], object=human_info[1], observation=human_info[2],
        inventory=human_info[3], task=human_info[4], 
    )
    all_messages = [system_message, human_message]

    response = gpt_query.llm(all_messages)
    answer = gpt_query.process_ai_message(response)
    if isinstance(answer, str):
        return False  # need to refine the return info
    else:
        exec_code = answer['code']
        with open(action_path, 'w') as f:
            f.write(exec_code)
        reload(action)
        action.act() # this function need to be refined
    
    target_states = answer['target']

    # states_to_bddl(target_states) #TODO: we need a function here

    # # verify bddl, return True or False, indicating the task succeeds or fails.

    # verify function
    value = []
    value.append(u.verify_inv(env, robot, target_states['inv']))
    for obj in target_states['obj_2']:
        value.append(u.verify_obj_2(obj[0], obj[1], obj[2]))
    for obj in target_states['obj_3']:
        value.append(u.verify_obj_3(obj[0], obj[1], obj[2], obj[3]))
    
    if False in value:
        return False
    else:
        return True
    
    


if __name__ == "__main__":
    main(scene_name="Merom_1_int",task_name="cook_bacon")
