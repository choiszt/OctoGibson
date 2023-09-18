import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Cook the sweet corn on the stove
    stove = registry(env,"stove_rgpphy_0")
    stockpot = registry(env,"stockpot_155")
    cook(robot, stockpot)
    donothing(env)
