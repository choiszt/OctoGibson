import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    toast = registry(env, "french_toast_188")
    MoveBot(env, toast, camera)
    donothing(env)
