import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, env):
    countertop = registry(env, "countertop_tpuwys_0")
    MoveBot(env, robot, countertop, camera)
    donothing(env)
