import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    waxpaper_191 = registry(env, "carpet_ctclvd_0")
    MoveBot(env, robot, waxpaper_191, camera)
    donothing(env)
