import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    tray = registry(env,"tray_156")
    if tray.distance > 2:
        stove = registry(env,"stove_rgpphy_0")
        MoveBot(env, robot, stove, camera)
        donothing(env)
    EasyGrasp(robot, tray)
