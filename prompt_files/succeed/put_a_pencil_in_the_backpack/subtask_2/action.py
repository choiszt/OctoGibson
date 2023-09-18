import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Put the colored pencil inside the backpack
    backpack_88 = registry(env,"backpack_88")
    colored_pencil_83 = registry(env,"colored_pencil_83")
    put_inside(robot, colored_pencil_83, backpack_88)
    donothing(env)
