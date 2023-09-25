import os
import json
import yaml
import sys;sys.path.append("/shared/liushuai/OmniGibson/prompt_files")
import omnigibson as og

from omnigibson.macros import gm
gm.USE_GPU_DYNAMICS = True
# gm.ENABLE_FLATCACHE = True
gm.ENABLE_OBJECT_STATES = True
from robot_action import *
# import prompt_files.action as action
from importlib import reload
import importlib
import env_utils_sim as eu 
from initial_pipeline import *
import time
from bddl_verification import *
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


def sim_process(args):
    try:    
        idx = args.idx
        with open('./EVLM_Task/val_15task.json') as f: #TODO change the path
            data = json.load(f)
        EVLM_name=sorted(list(data))[idx]
        if  True:
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
            save_path = eu.f_mkdir(os.path.join('./evaluation/data', gpt_task_name))
            main_target_states = task_data['target_states']
            og.log.info(main_target_states)
            removed_items = task_data['removed_item']

            heading="import os \nimport json\nimport yaml\nimport omnigibson as og\nfrom action_list import * \nfrom action_utils import *\n"
            config_filename="./prompt_files/bddl_task.yaml"
            cfg = yaml.load(open(config_filename, "r"), Loader=yaml.FullLoader)
            cfg["task"]["online_object_sampling"] = False
            cfg["scene"]["scene_model"] = scene_name
            cfg["task"]["activity_name"] = task_name
            og.log.info(cfg)
            # Load the environment
            try:
                env = og.Environment(configs=cfg, action_timestep=1/60., physics_timestep=1/60.)
            except:
                og.log.info("Loading Environment Error!!!")
                og.log.info(task_name, scene_name)
                with open("./evaluation/failed_task.json","r")as f:
                    finished_task = json.load(f)
                    finished_task[gpt_task_name] = "error"
                with open("./evaluation/failed_task.json","w")as f:
                    f.write(json.dumps(finished_task))  
                return 0
            
            robot = env.robots[0]
            camera= og.sim.viewer_camera

            mapping=camera._get_obs()['seg_instance'][1]
            PSG_dict={}
            for map in mapping:
                PSG_dict.update({str(map[0]):map[1]})
            with open(os.path.join(save_path,"PSG_mapping.json"),"w")as f:
                f.write(json.dumps(PSG_dict))

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
                        with open("./evaluation/failed_task.json","r")as f:
                            finished_task = json.load(f)
                            finished_task[gpt_task_name] = "failed"
                        with open("./evaluation/failed_task.json","w")as f:
                            f.write(json.dumps(finished_task))
                        eu.save_feedback(feedback_path, subtask, code, error, critic, reset, main_succeed)
                        env.close()
                        return 0
                    else:
                        subtask, code = answer['subtask'], answer['code']
                        # with open(f"./prompt_files/data/{gpt_task_name}/subtask_{subtask_iter}/action.py", 'w') as f:
                        #     f.write(heading)
                        #     f.write(code)
                        # time.sleep(2)
                        sys.path=list(set(sys.path))
                        if(subtask_iter!=1):
                            sys.path.remove(f"./evaluation/data/{gpt_task_name}/subtask_{subtask_iter-1}")
                        sys.path.append(f"./evaluation/data/{gpt_task_name}/subtask_{subtask_iter}")
                        import action
                        time.sleep(1)
                        try:
                            reload(action) #add a key to record the code whether is correct 
                            time.sleep(2)
                            action.act(robot,env,camera)
                            og.log.info("act...")
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
                    #     og.log.info(f"target_inv:{target_states['inventory']}")
                    #     og.log.info(f"inventory:{robot.inventory}")
                    #     if not value: #TODO need to fix the bug
                    #         error += f"{target_states['inventory']} is not in Inventory.\n"
                   
                    # for obj in target_states['obj_2']:
                    #     value = eu.verify_obj_2(env,obj[0], obj[1], obj[2])
                    #     if not value:
                    #         error += f"State {obj[1]} of object {obj[0]} is not {obj[2]}\n"
                    # #verify binary states
                    # for obj in target_states['obj_3']:
                    #     if obj[0] == "robot" or obj[2] == "robot":
                    #         continue
                    #     value = eu.verify_obj_3(env,obj[0], obj[1], obj[2],obj[3], f"./prompt_files/data/{gpt_task_name}/subtask_{subtask_iter}/action.py")
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
                #     path=f"/shared/liushuai/OmniGibson/prompt_files/data/{task_name}/subtask_{iter_num}"
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
                    signal=[]
                    target=main_target_states

                    for tar in target:
                        if len(tar)==3:
                            if verify_taskgoal(env,*tar):
                                signal.append(1)
                            else:
                                signal.append(0)
                        elif len(tar)==4:
                            if verify_binary_taskgoal(env,*tar):
                                signal.append(1)
                            else:
                                signal.append(0)
                    if 0 not in signal:
                        main_succeed = True
                        with open("./evaluation/failed_task.json","r")as f:
                            finished_task = json.load(f)
                            finished_task[gpt_task_name] = "succeed"
                        with open("./evaluation/failed_task.json","w")as f:
                            f.write(json.dumps(finished_task))                        
                        og.log.info(f"finish {task_name}!!!!! congrats!!!!!")
                        eu.save_feedback(feedback_path, subtask, code, error, critic, reset, main_succeed)
                        env.close()
                        return 0
                    else:
                        eu.save_feedback(feedback_path, subtask, code, error, critic, reset, main_succeed)
                else:
                    eu.save_feedback(feedback_path, subtask, code, error, critic, reset, main_succeed)
                
                if reset: #
                    if subtask_iter!=1:
                        for iter_num in range(1,subtask_iter):
                            path=f"./evaluation/data/{gpt_task_name}/subtask_{iter_num}"
                            with open(os.path.join(path,"feedback.json"))as f:
                                tmp_feedback=json.load(f)
                            if tmp_feedback['critic']=='succeed':
                                time.sleep(1)
                                module=importlib.import_module(f"data.{gpt_task_name}.subtask_{iter_num}.action")
                                og.log.info(f"data.{gpt_task_name}.subtask_{iter_num}.action retrieve")
                                module.act(robot,env,camera)   
                if subtask_iter>14:
                    #write json
                    og.log.info(f"already attempt {subtask_iter} time, it is too long!")
                    with open("./evaluation/failed_task.json","r")as f:
                        finished_task = json.load(f)
                        finished_task[gpt_task_name] = "failed"
                    with open("./evaluation/failed_task.json","w")as f:
                        f.write(json.dumps(finished_task))    
                    env.close()        
                    return 0
    except Exception as e:
        print(e)
        og.log.info(f"loop failed")
        with open("./evaluation/failed_task.json","r")as f:
            finished_task = json.load(f)
            finished_task[gpt_task_name] = "error"
        with open("./evaluation/failed_task.json","w")as f:
            f.write(json.dumps(finished_task)) 
        return 0

if __name__ == "__main__":
    args = parse_args()
    sim_process(args)