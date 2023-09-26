import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env):
    togglable = registry(env, "plate_189")
    sckdal_0 = registry('sckdale_0')
