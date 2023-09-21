import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Heat the meat
    pork_chop = registry(env,"pork_chop_188")
    oven = registry(env,"oven_wuinhm_0")
    MoveBot(env, robot, oven, camera)
    donothing(env)
    put_inside(robot, pork_chop, oven)
    donothing(env)
    toggle_on(robot, oven)
    donothing(env)
