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
import sys;sys.path.append("/shared/liushuai/OmniGibson")
import bddl
from verify_taskgoal import *
import argparse

def parse_args():
    description = "EVLM_sim_process"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('idx', type=int, help='Index for data entry')
    parser.add_argument("-l", "--/log/level", type=str, help="error log 1", required=True)
    parser.add_argument("-f", "--/log/fileLogLevel", type=str, help="error log 2", required=True)
    parser.add_argument("-o", "--/log/outputStreamLevel", type=str, help="error log 3", required=True)
    return parser.parse_args()

def _decomposed(self): #decomposed all the object in the env at the very beginning
    OG_results=[]
    parsed_objects=self.env.task.activity_conditions.parsed_objects
    OG_dict=self.env.task.load_task_metadata()["inst_to_name"] #format in OG E.g: floor.n.01_1 -> floors_hcqtge_0
    for key in parsed_objects.keys():
        for ele in parsed_objects[key]: #E.g:bacon.n.01_1
            if ele not in self.removed_items:
                OG_results.append(OG_dict[ele])

    return OG_results

def sim_process(args):   
    idx = args.idx
    with open('/shared/liushuai/OmniGibson/EVLM_Task/all.json') as f: #TODO change the path
        data = json.load(f)
    EVLM_name=sorted(list(data))[idx]
    if "train" in data[EVLM_name]['split']:
        task_name=data[EVLM_name]['task_name']
        gpt_name=data[EVLM_name]['detailed_name']
        # scene=data[EVLM_name]['env']
        og.log.info(idx)
        og.log.info(f"EVLM:{EVLM_name}")
        og.log.info(f"task_name:{task_name}")
        og.log.info(f"detailed_name:{gpt_name}")
        task_data = data[EVLM_name]
        task_name = task_data['task_name']
        gpt_task_name = task_data['detailed_name']
        scene_name = task_data['env']
        main_target_states = task_data['target_states']
        og.log.info(main_target_states)
        removed_items = task_data['removed_item']

        config_filename="/shared/liushuai/OmniGibson/prompt_files/bddl_task.yaml"
        cfg = yaml.load(open(config_filename, "r"), Loader=yaml.FullLoader)
        cfg["task"]["online_object_sampling"] = False
        cfg["scene"]["scene_model"] = scene_name
        cfg["task"]["activity_name"] = task_name
        og.log.info(cfg)
        # Load the environment
        try:
            env = og.Environment(configs=cfg, action_timestep=1/60., physics_timestep=1/60.)
            OG_results=[]
            parsed_objects=env.task.activity_conditions.parsed_objects
            OG_dict=env.task.load_task_metadata()["inst_to_name"] #format in OG E.g: floor.n.01_1 -> floors_hcqtge_0
            for key in parsed_objects.keys():
                for ele in parsed_objects[key]: #E.g:bacon.n.01_1
                    if ele not in removed_items:
                        OG_results.append(OG_dict[ele])

            with open("/shared/liushuai/OmniGibson/prompt_files/from_jingkang/scene_object.json","r")as f:
                scene_object=json.load(f)
                scene_object[EVLM_name]=OG_results
            with open("/shared/liushuai/OmniGibson/prompt_files/from_jingkang/scene_object.json","w")as f:
                f.write(json.dumps(scene_object))
        except:
            og.log.info("Loading Environment Error!!!")
            og.log.info(task_name, scene_name)
            with open("/shared/liushuai/OmniGibson/prompt_files/from_jingkang/val_task.json","r")as f:
                finished_task = json.load(f)
                finished_task[gpt_task_name] = "error"
            with open("/shared/liushuai/OmniGibson/prompt_files/from_jingkang/val_task.json","w")as f:
                f.write(json.dumps(finished_task))  
            return 0
    return 0
    # except:
    #     og.log.info(f"loop failed")
    #     with open("/shared/liushuai/OmniGibson/prompt_files/from_jingkang/val_task.json","r")as f:
    #         finished_task = json.load(f)
    #         finished_task[gpt_task_name] = "error"
    #     with open("/shared/liushuai/OmniGibson/prompt_files/from_jingkang/val_task.json","w")as f:
    #         f.write(json.dumps(finished_task)) 
    #     return 0

if __name__ == "__main__":
    args = parse_args()
    sim_process(args)