import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    bottom_grocery_shelf = registry(env, "bottle_of_cooking_oil_88")
    MoveBot(env, robot, bottom_grocery_shelf, camera)
    donothing(env)
