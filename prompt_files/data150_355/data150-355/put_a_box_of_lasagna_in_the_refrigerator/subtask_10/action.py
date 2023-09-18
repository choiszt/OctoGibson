import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Check if the box of lasagna is inside the refrigerator.
    box_of_lasagna = registry(env,"box_of_lasagna_85")
    fridge = registry(env,"fridge_xyejdx_0")
    if (box_of_lasagna, 'inside', fridge) in env.relations:
        print("The box of lasagna is already inside the refrigerator.")
    else:
        print("The box of lasagna is not inside the refrigerator.")
