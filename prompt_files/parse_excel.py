import pandas as pd
import json

data = pd.read_excel(io='./tasks.xlsx', sheet_name='I1.cooking')
print(data.keys())
task_name = data['BDDL_Task']
gpt_task = data['EVLM_Task']
target_states = data['Target States']
removed_item = data['Removed Items']
scene_name = data['Environment']
all_tasks = {}
for i in range(len(task_name)):
    if gpt_task[i] == 'NA':
        continue
    try:
        one_task = {}
        one_task['task_name'] = task_name[i]
        one_task['gpt_task'] = gpt_task[i]
        r = removed_item[i]
        r = r.split(',')
        for j in range(len(r)):
            r[j] = r[j].replace('[', '')
            r[j] = r[j].replace(' ', '')
            r[j] = r[j].replace(']', '')
        one_task['removed_item'] = r
        all_t = []
        t = target_states[i]
        t = t.split('\n')
        num_t = len(t)
        for ts in range(num_t):
            t_s = t[ts].split(',')
            for k in range(len(t_s)):
                t_s[k] = t_s[k].replace(' ','')
                t_s[k] = t_s[k].replace('[','')
                t_s[k] = t_s[k].replace(']','')
            all_t.append(t_s)
        one_task['target_states'] = all_t
        one_task['env'] = scene_name[i]
        all_tasks[gpt_task[i]] = one_task
    except: 
        pass
     
with open('test.json', 'w') as f:
     f.write(json.dumps(all_tasks))