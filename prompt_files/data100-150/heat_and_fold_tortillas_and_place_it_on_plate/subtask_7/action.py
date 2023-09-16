import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Place the tortilla from the inventory onto the stove
    stove_rgpphy_0 = registry(env,"stove_rgpphy_0")
    tortilla_153 = registry(env,"tortilla_153")
    put_ontop(robot, tortilla_153, stove_rgpphy_0)
    donothing(env)
