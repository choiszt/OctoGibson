import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the objects: cheese tart (pie), fridge, and plate.
    cheese_tart_85 = registry(env,"cheese_tart_85")
    fridge_xyejdx_0 = registry(env,"fridge_xyejdx_0")
    plate_87 = registry(env,"plate_87")
    
    # Subtask 2: Grasp the cheese tart from the plate.
    EasyGrasp(robot, cheese_tart_85)
    donothing(env)
