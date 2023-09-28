import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    leafy_lawn_276 = registry(env, "driveway_aipswu_0")
    MoveBot(env, robot, leafy_lawn_276, camera)
    donothing(env)
