import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the bottle of shampoo
    bottle_of_shampoo_190 = registry(env,"bottle_of_shampoo_190")
    MoveBot(env, robot, bottle_of_shampoo_190, camera)
    donothing(env)
