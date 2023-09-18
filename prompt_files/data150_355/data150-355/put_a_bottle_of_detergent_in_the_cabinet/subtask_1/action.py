import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the bottle of detergent.
    bottle_of_detergent_120 = registry(env, "bottle_of_detergent_120")
    EasyGrasp(robot, bottle_of_detergent_120)
    donothing(env)
