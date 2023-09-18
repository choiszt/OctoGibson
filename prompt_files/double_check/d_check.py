import json
with open("/shared/liushuai/OmniGibson/prompt_files/finished_task.json","r")as f:
    task=json.load(f)

with open("/shared/liushuai/OmniGibson/EVLM_Task/all.json","r")as f:
    tasklist=json.load(f)
    tasklists=sorted(tasklist.keys())


for key in task.keys():
    if task[key]=="error":
        print(key)
        idx=tasklists.index(key)
        print(idx) # task_name:idx