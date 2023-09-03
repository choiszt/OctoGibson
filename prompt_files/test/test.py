import os
import sys
import importlib
import env_utils_gpt as eu
import time

# subtask_iter = 4

# if subtask_iter!=1:
#     for iter_num in range(1,subtask_iter):
#         path=f"/home/dongyuhao/test/sub{iter_num}"
#         print(path)
#         sys.path.pop()
#         sys.path.append(path)
#         print(sys.path)
#         import 
#         action.act()  


def retrieve(num):
    base_path = "/home/dongyuhao/test"
    for i in range(1, num):
        params = importlib.import_module(f"sub{i}.action")
        time.sleep(1)
        params.act()

subtask_iter = 100

if subtask_iter!=1:
    for iter_num in range(1,subtask_iter):
        dir = eu.f_mkdir(f"sub{iter_num}")
        with open(os.path.join(dir, 'action.py'), 'w') as f:
            f.write(f"def act():\n\tprint({iter_num})")
        time.sleep(1)
        params = importlib.import_module(f"sub{iter_num}.action")
        params.act()    
        
        if iter_num == 10: 
            retrieve(10)
 
