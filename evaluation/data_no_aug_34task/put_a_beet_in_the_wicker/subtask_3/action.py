import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    leafylawwn = registry(env, "breakfast_table_idnnmz_0")
    MoveBot(env, robot, leafylawwn, camera)
    donothing(env)
