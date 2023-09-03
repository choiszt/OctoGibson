import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    #Subtask1: Move the robot closer to the fridge (within a meter range)
    fridge = registry(env, "fridge_dszchb_0")
    MoveBot(env, robot, fridge, camera)
    donothing(env)
