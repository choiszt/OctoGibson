import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    cheese_tart_box_86 = registry(env, "pizza_box_86")
    MoveBot(env, robot, cheese_tart_box_86, camera)
    donothing(env)
