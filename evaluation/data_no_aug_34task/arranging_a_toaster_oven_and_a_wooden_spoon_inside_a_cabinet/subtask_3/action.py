import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    top_cabinetry = registry(env, "door_ktydvs_0")
    close(robot, top_cabinetry)
    donothing(env)
