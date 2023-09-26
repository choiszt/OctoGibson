import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    bowl_195 = registry(env, "pebble_91")
    MoveBot(env, robot, bowl_195, camera)
