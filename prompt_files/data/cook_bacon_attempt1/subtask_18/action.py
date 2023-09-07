import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    fridge = registry(env,"fridge_xyejdx_0")
    MoveBot(env, robot, fridge, camera)
    donothing(env)
    tray = registry(env,"tray_156")
    put_ontop(robot, tray, fridge)
    donothing(env)
