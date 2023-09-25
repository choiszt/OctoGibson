import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    shopping_cart_kmgltg_1 = registry(env, "shopping_cart_kmgltg_1")
    MoveBot(env, robot, shopping_cart_kmgltg_1, camera)
    donothing(env)
