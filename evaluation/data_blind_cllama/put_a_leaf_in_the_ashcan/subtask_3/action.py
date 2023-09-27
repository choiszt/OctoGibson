import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    trash_can_281 = registry(env, "trash_can_276")
    MoveBot(env, robot, trash_can_281, camera)
    donothing(env)
