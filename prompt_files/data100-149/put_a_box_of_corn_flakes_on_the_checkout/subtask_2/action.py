import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the box of corn flakes from the shopping cart.
    box_of_corn_flakes_142 = registry(env,"box_of_corn_flakes_142")
    EasyGrasp(robot, box_of_corn_flakes_142)
    donothing(env)
