import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    toast_191 = registry(env, "french_toast_188")
    MoveBot(env, robot, toast_191, camera)
    donothing(env)
