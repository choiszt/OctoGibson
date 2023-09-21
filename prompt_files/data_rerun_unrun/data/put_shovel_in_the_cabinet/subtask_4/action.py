import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the shovel in the cabinet
    shovel = registry(env, "shovel_94")
    cabinet = registry(env, "bottom_cabinet_jrhgeu_0")
    put_inside(robot, shovel, cabinet)
    donothing(env)
