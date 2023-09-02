import pandas as pd
import json

data = pd.read_excel(io='./BEHAVIOR_TASKS_ICLR.xlsx')
task_name = data['TASK NAME']
gpt_task = data['GPT TASK NAME']
target_states = data['Target States']
removed_item = data['Removed Item']
print(task_name)
all_tasks = {}
for i in range(len(task_name)):
     one_task = {}
     one_task['task_name'] = task_name[i]
     one_task['gpt_task'] = gpt_task[i]
     r = removed_item[i]
     r = r.split(',')
     for j in range(len(r)):
          r[j] = r[j].replace('{', '')
          r[j] = r[j].replace(' ', '')
          r[j] = r[j].replace('\'', '')
          r[j] = r[j].replace('}', '')
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
     all_tasks[task_name[i]] = one_task
     
with open('test.json', 'w') as f:
     f.write(json.dumps(all_tasks))