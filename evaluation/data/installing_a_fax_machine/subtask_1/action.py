import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    modem_279 = registry(env, "oven_wuinhm_0")
    MoveBot(env, robot, modem_279, camera)
    donothing(env)
