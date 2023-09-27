import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    gas_tak_193 = registry(env, "tank_88")
    MoveBot(env, robot, gas_tak_193, camera)
    donothing(env)
