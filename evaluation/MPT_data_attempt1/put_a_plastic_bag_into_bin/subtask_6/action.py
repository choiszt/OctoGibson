import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    trash_can = registry(trash_can, 'trash-can_79')
    MoveBot(env, robot, trash_can, camera)
    donothing(env)
