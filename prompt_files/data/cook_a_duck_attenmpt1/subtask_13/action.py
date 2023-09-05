import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    duck = registry(env,"duck_171")
    oven = registry(env,"oven_wuinhm_0")
    put_inside(robot, duck, oven)
    donothing(env)
