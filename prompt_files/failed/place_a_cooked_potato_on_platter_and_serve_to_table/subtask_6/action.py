import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the potato inside the oven.
    potato = registry(env, "potato_89")
    oven = registry(env, "oven_wuinhm_0")
    put_inside(robot, potato, oven)
    donothing(env)
