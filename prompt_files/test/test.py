import os
import sys
import importlib

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

subtask_iter = 4

if subtask_iter!=1:
    for iter_num in range(1,subtask_iter):
        params = importlib.import_module(f"sub{iter_num}.action")
        params.act()      
