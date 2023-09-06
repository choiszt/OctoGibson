import json
import os
import random 
import numpy as np

import base64
import cv2

def get_img_json(base_path, task_name, sub_path, image_name):    
    image = cv2.imread(os.path.join(base_path, task_name, sub_path, image_name), cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))

    # 将图像转换为 Base64 格式
    _, buffer = cv2.imencode('.png', image)
    base64_image = base64.b64encode(buffer)
    # 将 Base64 编码转换为字符串
    return base64_image.decode()


base_path = '/home/dongyuhao/data'

all_data = {}
all_rel = {}
all_images = {}
for dir in os.listdir(base_path):
    task_path = os.path.join(base_path, dir)
    
    # cal subtask number
    subtask_num = 0
    for sub_dir in os.listdir(task_path):
        sub_path = os.path.join(task_path, sub_dir)
        if len(os.listdir(sub_path)) == 0:
            break
        else:
            subtask_num += 1
            
    for sub_dir in os.listdir(task_path):
        sub_path = os.path.join(task_path, sub_dir)
        if len(os.listdir(sub_path)) == 0:
            continue
        else:
            #KEY
            name = dir + '_' + sub_dir
            
            #CRITIC
            with open(os.path.join(sub_path, 'feedback.json')) as f0:
                reward = 0
                feedback = json.load(f0)['critic']
                if feedback == 'succeed':
                    reward = 1
            
            #INSTRUCTION
            with open(os.path.join(sub_path, 'input.json')) as f1:
                input_data = json.load(f1)['input']
                input_data = input_data[input_data.find('Inventory'):]
                input_str = input_data
                
            #RESPONSE
            with open(os.path.join(sub_path, 'response.json')) as f2:
                response = json.load(f2)['response']
                response_str = 'Explain:\n' + response['explain'] + '\nSubtask:' + response['subtask'] + '\nCode:\n' + response['code'] + \
                                '\nInventory:' + response['inventory'] + '\nTarget States:\n'
                target_num = 0
                for data in response['obj_2']:
                    response_str += f'({chr(target_num+97)}) {data}\n'
                    target_num += 1
                for data in response['obj_3']:
                    response_str += f'({chr(target_num+97)}) {data}\n'
                    target_num += 1
                    
            #IMAGEID
            images = [image for image in os.listdir(sub_path) if 'rgb' in image]
            imageids = [name + '_' + image.strip('.png') for image in os.listdir(sub_path) if 'rgb' in image]
            for k, i in enumerate(imageids):
                all_images[i] = get_img_json(base_path, task_path, sub_dir, images[k])
            
            #RELID
            ids = os.listdir(task_path)
            if subtask_num < 5:
                rel_id = [dir + '_' + id for id in ids[:subtask_num]]
            else:
                idx = random.sample(ids[:subtask_num], 4)
                rel_id = [dir + '_' + idx[i] for i in range(4)]
            
        all_data[name] = {}
        all_data[name]["instruction"] = input_str
        all_data[name]["answer"] = response_str
        all_data[name]["image_ids"] = imageids
        all_data[name]["rel_ins_ids"] = rel_id
        all_data[name]['reward'] = reward

        all_rel[name] = rel_id
        
dataset = {}
dataset['meta'] = {'version':'v1', 'author':'dongyuhao', 'date':'2023-09-06'}
dataset['data'] = all_data
with open('test.json', 'w') as f:
    f.write(json.dumps(dataset))
    
with open('test_train.json', 'w') as f:
    f.write(json.dumps(all_rel))
    
with open('test_images.json', 'w') as f:
    f.write(json.dumps(all_images))




