import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the laptop
    laptop_278 = registry(env,"laptop_278")
    EasyGrasp(robot, laptop_278)
    donothing(env)
