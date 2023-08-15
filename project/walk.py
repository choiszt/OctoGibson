import os 
import json

def walk_dir(path):
    pair = {}
    dirs = os.listdir(path)
    for dir in dirs:
        files = os.listdir(os.join(path, dir, 'json'))
        for file in files:
            task = file.split(dir)[1]
            task = task.split('_0')[0]
            pair[task] = dir
    with open('task_scene.json', 'w') as f:
        f.write(json.dumps(pair, indent=4))
    return pair

if __name__ == '__main__':
    # name = 'Scene_a_b_0_0.json'
    # a = name.split('Scene_')[1]
    # b = a.split('_0')[0]
    # print(b)
    
    # walk_dir(path)
