import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    stove = registry(env,"stove_rgpphy_0")
    tray = registry(env,"tray_156")
    put_ontop(robot, tray, stove)
    donothing(env)
