import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the box of lasagna inside the refrigerator.
    box_of_lasagna_85 = registry(env,"box_of_lasagna_85")
    fridge_xyejdx_0 = registry(env,"fridge_xyejdx_0")
    put_inside(robot, box_of_lasagna_85, fridge_xyejdx_0)
    donothing(env)
