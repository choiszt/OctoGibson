import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    bowl_194 = registry(env, "olive_171")
    MoveBot(env, robot, bowl_194, camera)
