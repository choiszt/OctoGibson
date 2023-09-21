import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the beer keg
    beer_keg_142 = registry(env,"beer_keg_142")
    checkout_counter_sckdal_0 = registry(env,"checkout_counter_sckdal_0")
    MoveBot(env, robot, beer_keg_142, camera)
    donothing(env)
