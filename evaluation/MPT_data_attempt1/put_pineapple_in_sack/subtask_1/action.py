import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    fruit = registry(env, "credit_card_143")
    MoveBot(env, 'robot', fruit, camera)
    donothing(env)
