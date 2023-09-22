import json
import os
with open("/shared/liushuai/OmniGibson/EVLM_Task/all_val.json","r")as f:
    task=json.load(f)
allobject={}
for ele in task.keys():
    scene_name=task[ele]['env']
    bddl_name=task[ele]['task_name']
    jsonpath=f"{scene_name}_task_{bddl_name}_0_0_template.json"
    targetpath=f"/home/liushuai/.conda/envs/omni/lib/python3.7/site-packages/omnigibson-0.2.0-py3.7.egg/omnigibson/data/og_dataset/scenes/{scene_name}/json/{jsonpath}"

    detailed_name=task[ele]['detailed_name']

    with open(targetpath,"r")as f:
        object=json.load(f)
    allobject.update({detailed_name:list(object['objects_info']['init_info'].keys())})
with open("/shared/liushuai/OmniGibson/prompt_files/for_jingkang/all_object.json","w")as f:
    f.write(json.dumps(allobject))