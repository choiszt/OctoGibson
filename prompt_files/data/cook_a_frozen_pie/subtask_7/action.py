import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    cheese_tart = registry(env,"cheese_tart_188")
    oven = registry(env,"oven_wuinhm_0")
    put_inside(robot, cheese_tart, oven)
    donothing(env)
