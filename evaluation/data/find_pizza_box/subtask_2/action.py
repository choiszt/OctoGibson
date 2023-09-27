import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    oven_wuinhm_000 = registry(env, "oven_wuinhm_0")
    open(robot, env)
    donothing(env)
