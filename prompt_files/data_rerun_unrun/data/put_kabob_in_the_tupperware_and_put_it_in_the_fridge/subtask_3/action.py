import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move the robot to the fridge
    fridge_xyejdx_0 = registry(env,"fridge_xyejdx_0")
    MoveBot(env, robot, fridge_xyejdx_0, camera)
    donothing(env)
    # Subtask 6: Open the fridge
    open(robot, fridge_xyejdx_0)
    donothing(env)
