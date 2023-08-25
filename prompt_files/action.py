import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(env, robot, camera):
    fridge = registry(env, "fridge_xyejdx_0")
    MoveBot(env, robot, fridge, camera)
    donothing(env)
    open(robot, fridge)
    donothing(env)
