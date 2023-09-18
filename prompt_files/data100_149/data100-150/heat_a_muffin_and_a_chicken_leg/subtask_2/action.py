import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take out a muffin from the fridge
    muffin = registry(env,"muffin_88")
    EasyGrasp(robot, muffin)
    donothing(env)
