import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    open(robot, env)
    donothing(env)
