import json
import os
import prompt_files.env_utils_gpt as eu
from excecute_env import exec

openai_api_key = "YOUR_API_KEY"

with open("one_scene.json", 'r') as f:
    data = json.load(f)

for k, v in data.items():
    base_path = eu.f_mkdir(os.path.join('./data', str(k)))
    exec(task_name=k, scene_name=v, save_path=base_path,
         action_path='./action.py', openai_api_key=openai_api_key)
    