import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the clothes dryer.
    clothes_dryer = registry(env, "clothes_dryer_zlmnfg_0")
    MoveBot(env, robot, clothes_dryer, camera)
