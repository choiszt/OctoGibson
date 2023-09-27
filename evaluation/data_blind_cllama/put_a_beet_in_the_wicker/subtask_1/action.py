import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    beet_275 = registry(env, "beet_277")
    MoveBot(env, robot, beet_275, camera)
    donothing(env)
