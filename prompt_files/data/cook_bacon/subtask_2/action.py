import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Subtask 1: Take the tray containing bacon out from the fridge.
    tray = registry(env, "tray_156")
    EasyGrasp(robot, tray)
    donothing(env)
