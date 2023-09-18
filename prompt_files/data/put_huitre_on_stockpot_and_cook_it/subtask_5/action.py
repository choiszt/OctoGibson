import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Cook the oyster
    # Assuming the oyster is on the stockpot
    oyster = registry(env,"oyster_201")
    cook(robot, oyster)
    donothing(env)
