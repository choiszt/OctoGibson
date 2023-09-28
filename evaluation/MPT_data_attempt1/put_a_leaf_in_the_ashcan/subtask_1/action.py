import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    leaf_279 = registry(env, "leaf_277")
    MoveBot(env, robot, leaf_279, camera)
    donothing(env)
