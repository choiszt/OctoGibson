import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Grasp the cooked steak from the frying pan
    steak = registry(env,"steak_201")
    EasyGrasp(robot, steak)
    donothing(env)
