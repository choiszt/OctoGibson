import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Take the saucepot from the countertop
    saucepot = registry(env, "saucepot_87")
    EasyGrasp(robot, saucepot)
    donothing(env)
