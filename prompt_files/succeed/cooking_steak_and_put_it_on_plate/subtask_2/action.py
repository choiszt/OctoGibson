import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the steak out of the fridge
    steak = registry(env,"steak_201")
    EasyGrasp(robot, steak)
    donothing(env)
