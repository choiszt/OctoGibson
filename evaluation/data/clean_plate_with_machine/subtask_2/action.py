import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    machine_172 = registry(env, "tablefork_172")
    MoveBot(env, robot, machine_172, camera)
    donothing(env)
