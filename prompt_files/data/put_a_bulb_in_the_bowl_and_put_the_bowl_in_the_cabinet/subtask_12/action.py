import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Put the mixing bowl in the top cabinet
    mixing_bowl_173 = registry(env,"mixing_bowl_173")
    top_cabinet_dmwxyl_2 = registry(env,"top_cabinet_dmwxyl_2")
    put_inside(robot, mixing_bowl_173, top_cabinet_dmwxyl_2)
    donothing(env)
