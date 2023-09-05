import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    oven = registry(env,"oven_wuinhm_0")
    MoveBot(env, robot, oven, camera)
    donothing(env)
