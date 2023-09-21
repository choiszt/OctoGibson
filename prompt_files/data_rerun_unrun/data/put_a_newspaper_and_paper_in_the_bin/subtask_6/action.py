import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Grasp the notepad
    notepad_172 = registry(env,"notepad_172")
    EasyGrasp(robot, notepad_172)
    donothing(env)
