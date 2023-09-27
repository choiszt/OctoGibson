import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    suitcase_279 = registry(env, "suitcase_279")
    MoveBot(env, robot, suitcase_279, camera)
