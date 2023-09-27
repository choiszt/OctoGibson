import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    clothes_dryer = registry(env, "tree_dyymaq_0")
    open(robot, clothes_dryer)
    donothing(env)
