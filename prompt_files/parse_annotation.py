import json

def parse():
    with open('./test.json') as f:
        data = json.load(f)
        
    original_task = data['task_name']
    gpt_task = data['gpt_task']
    remove_item = data['removed_ietm']
    target_states = data['target_states']
    obj_2 = []
    obj_3 = []
    for i in range(len(target_states)):
        if len(target_states[i]) == 3:
            obj_2.append(target_states[i])
        if len(target_states[i]) == 4:
            obj_3.append(target_states[i])
    return original_task, gpt_task, remove_item, target_states, obj_2, obj_3

