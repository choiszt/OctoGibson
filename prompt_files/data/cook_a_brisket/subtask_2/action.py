import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    fridge = registry(env, "fridge_dszchb_0")
    brisket = registry(env, "brisket_189")
    # Subtask 1: Move the robot closer to the fridge
    MoveBot(env, robot, fridge, camera)
    donothing(env)
