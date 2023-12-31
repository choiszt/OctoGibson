import json

def parse(num):
    with open('/shared/liushuai/OmniGibson/EVLM_Task/task_0908.json', 'r') as f:
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
        parsed_data = {}
        parsed_data['bddl'] = bddl_task
        parsed_data['gpt'] = gpt_task
        parsed_data['scene'] = scene_name
        parsed_data['removed'] = removed_items
        parsed_data['target_states'] = target_states
    return parsed_data