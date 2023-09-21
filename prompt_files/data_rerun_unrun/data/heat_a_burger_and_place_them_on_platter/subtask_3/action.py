import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Heat the burger
    hamburger = registry(env,"hamburger_85")
    heat(robot, hamburger)
    donothing(env)
