import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, robot):
    cutting_recycling_bin = registry(env, "recycling_bin_188")
    MoveBot(env, robot, cutting_recycling_bin, camera)
    donothing(env)
