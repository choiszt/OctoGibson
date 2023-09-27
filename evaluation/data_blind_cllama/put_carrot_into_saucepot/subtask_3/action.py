import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    saucepot_170 = registry(env, "saucepot_150")
    MoveBot(env, robot, saucepot_170, camera)
    donothing(env)
