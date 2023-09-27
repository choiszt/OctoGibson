import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    floor = registry(env, "floors_jniagb_0")
    MoveBot(env, robot, floor, camera)
    donothing(env)
