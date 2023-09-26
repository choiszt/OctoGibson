import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    cab_1 = registry(env)
    MoveBot(env, robot, cab_1, camera)
    donothing(env)
