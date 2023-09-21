import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the box of baking soda in the cabinet.
    box_of_baking_soda_170 = registry(env,"box_of_baking_soda_170")
    top_cabinet_dmwxyl_2 = registry(env,"top_cabinet_dmwxyl_2")
    put_inside(robot, box_of_baking_soda_170, top_cabinet_dmwxyl_2)
    donothing(env)
