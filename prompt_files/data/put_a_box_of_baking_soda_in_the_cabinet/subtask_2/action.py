import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the box of baking soda.
    box_of_baking_soda_170 = registry(env,"box_of_baking_soda_170")
    EasyGrasp(robot, box_of_baking_soda_170)
    donothing(env)
