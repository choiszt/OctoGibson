import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the glove in the cabinet
    kid_glove_122 = registry(env,"kid_glove_122")
    top_cabinet_dmwxyl_3 = registry(env,"top_cabinet_dmwxyl_3")
    put_inside(robot, kid_glove_122, top_cabinet_dmwxyl_3)
    donothing(env)
