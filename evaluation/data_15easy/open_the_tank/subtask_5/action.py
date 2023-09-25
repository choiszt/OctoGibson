import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    environment = registry(env, "washer_omeuop_0")
    unfold(robot, robot, environment)
    donothing(env)
