import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the bottle of detergent in the cabinet.
    bottle_of_detergent_120 = registry(env, "bottle_of_detergent_120")
    top_cabinet_dmwxyl_3 = registry(env, "top_cabinet_dmwxyl_3")
    put_inside(robot, bottle_of_detergent_120, top_cabinet_dmwxyl_3)
    donothing(env)
