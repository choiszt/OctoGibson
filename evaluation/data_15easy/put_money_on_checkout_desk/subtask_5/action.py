import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    camera = registry(env, "cash_register_tggwud_0")
    MoveBot(env, camera, camera)
    donothing(env)
