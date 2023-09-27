import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    grocery_shelfs = registry(env, "grocery_shelf_sjmdri_1")
    shopping_cart = registry(env, "shopping_cart_kmgltg_1")
