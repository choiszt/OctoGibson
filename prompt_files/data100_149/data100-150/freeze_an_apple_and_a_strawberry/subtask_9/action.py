import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Move the robot to the tray
    tray = registry(env, "tray_90")
    MoveBot(env, robot, tray, camera)
    donothing(env)
