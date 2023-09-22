import json
import os
def get_allobject():
    with open("/shared/liushuai/OmniGibson/EVLM_Task/all_val.json","r")as f:
        task=json.load(f)
    allobject={}
    for ele in sorted(task.keys()):
        scene_name=task[ele]['env']
        bddl_name=task[ele]['task_name']
        jsonpath=f"{scene_name}_task_{bddl_name}_0_0_template.json"
        targetpath=f"/home/liushuai/.conda/envs/omni/lib/python3.7/site-packages/omnigibson-0.2.0-py3.7.egg/omnigibson/data/og_dataset/scenes/{scene_name}/json/{jsonpath}"

        detailed_name=task[ele]['detailed_name']

        with open(targetpath,"r")as f:
            object=json.load(f)
        allobject.update({ele:list(object['objects_info']['init_info'].keys())})
    with open("/shared/liushuai/OmniGibson/prompt_files/for_jingkang/all_object.json","w")as f:
        f.write(json.dumps(allobject))


with open("/shared/liushuai/OmniGibson/prompt_files/for_jingkang/all_object.json",'r')as f:
    all_object=json.load(f)

with open("/shared/liushuai/OmniGibson/prompt_files/for_jingkang/scene_object.json","r")as f:
    sim_object=json.load(f)

filtered_dict={}

def get_val_unique_object():
    total_obj=[]
    unique_obj=[]
    for ele in all_object.keys():
        for obj in all_object[ele]:
            total_obj.append(obj)
    total_obj=list(set(total_obj)) 

    for uni_obj in total_obj:
        unique_obj.append(uni_obj.split("_")[0])

    unique_obj=list(set(unique_obj))

wiped_dict={}
for ele in all_object.keys():
    json_list=[]
    unique_list=[]
    for obj in all_object[ele]:
        if obj.split("_")[0] not in unique_list:
            unique_list.append(obj.split("_")[0])
            json_list.append(obj)
            wiped_dict.update({ele:json_list})

with open("/shared/liushuai/OmniGibson/prompt_files/for_jingkang/wiped_object.json","w")as f:
    f.write(json.dumps(wiped_dict))       



for ele in sim_object.keys():
    templist=[]
    for obj in sim_object[ele]:
        if obj in all_object[ele]:
            templist.append(obj)
    filtered_dict.update({ele:templist})
