import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    money = (env, 'money_142', 'Themoney_143')
    MoveBot(env, robot, camera, camera)
    donothing(env)