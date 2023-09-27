import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    case = registry(env, "suitcase_279")
    MoveBot(env, 'robot', case, camera)
    donothing(env)
