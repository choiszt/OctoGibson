import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    cabinet = registry(env, "bottom_cabinet_bamfsz_0")
    MoveBot(env, robot, cabinet, camera)
    donothing(env)
