import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    stank = registry(env, "tank_88")
    MoveBot(open(robot), stank, camera)
    donothing(env)
