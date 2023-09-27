import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    water_bottom_83 = registry(env, "water_filter_90")
    toggle_on(robot, water_bottom_83)
