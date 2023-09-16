import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp the apple from the bowl
    apple = registry(env, "apple_88")
    EasyGrasp(robot, apple)
    donothing(env)
