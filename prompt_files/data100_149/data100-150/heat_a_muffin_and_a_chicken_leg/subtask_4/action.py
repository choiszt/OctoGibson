import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Heat the muffin
    muffin = registry(env,"muffin_88")
    heat(robot, muffin)
    donothing(env)
