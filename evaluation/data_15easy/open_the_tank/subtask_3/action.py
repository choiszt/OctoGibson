import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    add_operational_function = registry(env, "water_filter_90")
    MoveBot(env, 'bot', add_operational_function, camera)
    donothing(env)
