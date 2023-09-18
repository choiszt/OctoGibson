import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Toggle on the stove
    stove_rgpphy_0 = registry(env,"stove_rgpphy_0")
    toggle_on(robot, stove_rgpphy_0)
    donothing(env)
