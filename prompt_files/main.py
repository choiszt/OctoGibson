import json
import os
import env_utils as eu
from excecute_env import exec

openai_api_key = "YOUR_API_KEY"

with open("one_scene.json", 'r') as f:
    data = json.load(f)

for k, v in data.items():
    base_path = eu.f_mkdir(os.path.join('./data', str(k)))
    json_path = eu.f_mkdir(base_path, 'json_files')
    save_path = eu.f_mkdir(base_path, 'training_data')
    exec(task_name=k, scene_name=v, json_path=json_path, save_path=save_path,
         action_path='./action.py', openai_api_key=openai_api_key)
    