import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the firewood
    firewood_275 = registry(env,"firewood_275")
    coffee_table_ejlbho_0 = registry(env,"coffee_table_ejlbho_0")
    MoveBot(env, robot, firewood_275, camera)
    donothing(env)
