import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the folder out of the cabinet
    folder_190 = registry(env,"folder_190")
    EasyGrasp(robot, folder_190)
    donothing(env)
