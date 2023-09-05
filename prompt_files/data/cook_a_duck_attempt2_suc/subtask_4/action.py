import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take the duck out of the fridge
    duck = registry(env,"duck_171")
    EasyGrasp(robot, duck)
    donothing(env)
