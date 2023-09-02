import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Registration
    brisket = registry(env, "brisket_189")
    # Subtask 1: Move to in front of the fridge
    fridge = registry(env, "fridge_dszchb_0")
    MoveBot(env, robot, fridge, camera)
    donothing(env)
    # Subtask 2: Obtain the brisket from the fridge
    EasyGrasp(robot, brisket)
    donothing(env)
