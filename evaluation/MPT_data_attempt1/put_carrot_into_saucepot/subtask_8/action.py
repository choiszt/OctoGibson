import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    saucespan_150 = registry(env, "saucepot_150")
    MoveBot(env, robot, saucespan_150, camera)
    donothing(env)
