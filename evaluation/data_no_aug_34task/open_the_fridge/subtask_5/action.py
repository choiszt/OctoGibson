import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    fridge = registry(env, "fridge_xyejdx_0")
    MoveBot(camera, fridge, camera)
    donothing(env)
