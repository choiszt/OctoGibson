import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Put the bowl in the cabinet
    top_cabinet_dmwxyl_2 = registry(env,"top_cabinet_dmwxyl_2")
    mixing_bowl_173 = registry(env,"mixing_bowl_173")
    put_inside(robot, mixing_bowl_173, top_cabinet_dmwxyl_2)
    donothing(env)
