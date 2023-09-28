import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    fridgerobot_3 = registry(env, "fridge_xyejdx_0")
    MoveBot(robot, fridgerobot_3, env, camera)
    donothing(env)
