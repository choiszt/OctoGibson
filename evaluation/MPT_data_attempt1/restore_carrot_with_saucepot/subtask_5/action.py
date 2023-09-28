import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    oven = registry(env, "stove_rgpphy_0")
    open(robot, oven)
    donothing(env)
