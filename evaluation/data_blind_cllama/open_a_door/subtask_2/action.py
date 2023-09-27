import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    door = registry(env, "door_ktydvs_0")
    MoveBot(env, robot, door, camera)
    donothing(env)
