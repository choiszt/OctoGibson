import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the shopping cart
    shopping_cart_kmgltg_0 = registry(env,"shopping_cart_kmgltg_0")
    MoveBot(env, robot, shopping_cart_kmgltg_0, camera)
    donothing(env)
