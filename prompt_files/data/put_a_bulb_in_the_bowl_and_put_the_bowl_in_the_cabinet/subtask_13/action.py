import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the bulb.
    daffodil_bulb_170 = registry(env,"daffodil_bulb_170")
    MoveBot(env, robot, daffodil_bulb_170, camera)
    donothing(env)
