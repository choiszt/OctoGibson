import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the kale out of the fridge
    kale = registry(env, "kale_85")
    EasyGrasp(robot, kale)
    donothing(env)
