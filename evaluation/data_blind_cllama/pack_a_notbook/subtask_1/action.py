import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    grocery_shelf = registry(env, "shelf_owvfik_0")
    MoveBot(env, robot, grocery_shelf, camera)
    donothing(env)
