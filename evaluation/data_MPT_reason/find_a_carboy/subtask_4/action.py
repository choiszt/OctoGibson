import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    fridge = 'fridge_{0'.format(env)
    registry(robot, 0.0, env)
