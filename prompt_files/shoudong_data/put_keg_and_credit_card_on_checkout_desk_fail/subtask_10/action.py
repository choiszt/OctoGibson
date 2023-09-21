import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the beer keg
    beer_keg_142 = registry(env,"beer_keg_142")
    EasyGrasp(robot, beer_keg_142)
    donothing(env)
