import json
with open("/shared/liushuai/OmniGibson/EVLM_Task/new913.json","r")as f:
    task=json.load(f)

with open("/shared/liushuai/OmniGibson/prompt_files/example/t.txt","w+")as f:
    pass
for i in range(34):
    EVLM_name=sorted(list(task))[i]
    task_name=task[EVLM_name]['task_name']
    gpt_name=task[EVLM_name]['gpt_task']
    scene=task[EVLM_name]['env']

    with open("/shared/liushuai/OmniGibson/prompt_files/example/t.txt","a+")as f:
        f.write(str(gpt_name)+'\n')