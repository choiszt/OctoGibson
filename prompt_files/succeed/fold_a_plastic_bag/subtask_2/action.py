import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Open the clothes dryer
    clothes_dryer = registry(env, "clothes_dryer_zlmnfg_0")
    open(robot, clothes_dryer)
    donothing(env)
