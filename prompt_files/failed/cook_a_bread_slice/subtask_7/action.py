import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp a bread slice
    bread_slice_86 = registry(env,"bread_slice_86")
    EasyGrasp(robot, bread_slice_86)
    donothing(env)
