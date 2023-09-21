import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the carrot out of the fridge
    carrot = registry(env,"carrot_151")
    EasyGrasp(robot, carrot)
    donothing(env)
