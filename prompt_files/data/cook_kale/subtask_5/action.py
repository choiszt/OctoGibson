import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Put the saucepot into the oven
    saucepot = registry(env,"saucepot_87")
    oven = registry(env,"oven_wuinhm_0")
    EasyGrasp(robot, saucepot)
    donothing(env)
    put_inside(robot, saucepot, oven)
    donothing(env)
