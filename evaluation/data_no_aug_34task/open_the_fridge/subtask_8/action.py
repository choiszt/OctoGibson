import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env):
    door = registry(env, "door_ktydvs_0")
    open(robot, door)
    donothing(env)
