import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    ground = MoveBot(env, 'ground')
    MoveBot(env, robot, robot, camera)
    donothing(env)
