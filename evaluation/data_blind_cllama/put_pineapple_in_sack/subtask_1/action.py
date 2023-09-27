import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    grocery_shelf_prtqlw_2 = registry(env, "grocery_shelf_rowulr_7")
    MoveBot(env, robot, grocery_shelf_prtqlw_2, camera)
    donothing(env)
