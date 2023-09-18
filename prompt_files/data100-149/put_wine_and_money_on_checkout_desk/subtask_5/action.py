import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move to the shopping cart.
    shopping_cart = registry(env, "shopping_cart_kmgltg_1")
    MoveBot(env, robot, shopping_cart, camera)
    donothing(env)
