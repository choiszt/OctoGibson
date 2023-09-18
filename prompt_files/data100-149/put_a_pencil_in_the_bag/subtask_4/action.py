import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the colored_pencil_277 inside the suitcase_276
    colored_pencil_277 = registry(env,"colored_pencil_277")
    suitcase_276 = registry(env,"suitcase_276")
    put_inside(robot, colored_pencil_277, suitcase_276)
    donothing(env)
