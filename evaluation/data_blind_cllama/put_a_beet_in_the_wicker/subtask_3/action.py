import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    wicker_basket = registry(env, "wicker_basket_278")
    MoveBot(env, robot, wicker_basket, camera)
    donothing(env)
