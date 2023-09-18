import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the folder (with the document inside) back into the cabinet
    folder_190 = registry(env,"folder_190")
    bottom_cabinet_nddvba_0 = registry(env,"bottom_cabinet_nddvba_0")
    put_inside(robot, folder_190, bottom_cabinet_nddvba_0)
    donothing(env)
