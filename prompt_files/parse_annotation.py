import json

def parse(num):
    with open('./test.json', 'r') as f:
        data = json.load(f)
    
    for k, v in enumerate(data):
        if k != num:
            continue
        task_data = data[v]
        bddl_task = task_data['task_name']
        gpt_task = task_data['gpt_task']
        scene_name = task_data['env']
        removed_items = task_data['removed_item']
        target_states = task_data['target_states']
        obj_2 = []
        obj_3 = []
        for i in range(len(target_states)):
            if len(target_states[i]) == 3:
                obj_2.append(target_states[i])
            if len(target_states[i]) == 4:
                obj_3.append(target_states[i])
        parsed_data = {}
        parsed_data['bddl'] = bddl_task
        parsed_data['gpt'] = gpt_task
        parsed_data['scene'] = scene_name
        parsed_data['removed'] = removed_items
        parsed_data['obj_2'] = obj_2
        parsed_data['obj_3'] = obj_3
    return parsed_data