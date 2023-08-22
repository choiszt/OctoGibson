import json
from excecute_env import exec

openai_api_key = "YOUR_API_KEY"

with open("one_scene.json", 'r') as f:
    data = json.load(f)

for k, v in data.items():
    exec(task_name=k, scene_name=v, json_path="./information.json", save_path='./action_data',
         action_path='./action.py', openai_api_key=openai_api_key)
    