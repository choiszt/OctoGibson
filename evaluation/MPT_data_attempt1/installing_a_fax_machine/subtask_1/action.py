import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    fax_device = registry(env, "facsimile_188")
    MoveBot(env, 'robot', fax_device, camera)
    donothing(env)
