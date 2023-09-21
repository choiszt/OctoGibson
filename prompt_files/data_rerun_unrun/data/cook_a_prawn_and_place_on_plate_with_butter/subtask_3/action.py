import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take the butter from the fridge
    butter = registry(env,"butter_208")
    EasyGrasp(robot, butter)
    donothing(env)
