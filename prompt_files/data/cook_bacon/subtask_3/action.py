import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the tray with bacon on the stove.
    stove = registry(env, "stove_rgpphy_0")
    tray = registry(env, "tray_156")
    put_ontop(robot, tray, stove)
    donothing(env)
