import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    cabintask_94 = registry(env, "top_cabinet_dmwxyl_0")
    MoveBot(env, robot, cabintask_94, camera)
    donothing(env)
