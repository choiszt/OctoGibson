import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    countertop_tpuwys_2 = registry(env, "stove_rgpphy_0")
    MoveBot(env, robot, countertop_tpuwys_2, camera)
    donothing(env)
