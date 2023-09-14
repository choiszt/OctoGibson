import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the tank
    tank_88 = registry(env,"tank_88")
    MoveBot(env, robot, tank_88, camera)
    donothing(env)
    # Subtask 2: Close the tank
    close(robot, tank_88)
    donothing(env)
