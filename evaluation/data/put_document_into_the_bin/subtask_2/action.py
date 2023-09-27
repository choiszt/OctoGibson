import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    recycling_bin_188 = registry(env, "recycling_bin_188")
    MoveBot(env, robot, recycling_bin_188, camera)
    donothing(env)
