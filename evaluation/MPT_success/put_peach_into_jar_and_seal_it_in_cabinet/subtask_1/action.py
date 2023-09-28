import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    peaches_173 = registry(env, "peach_173")
    MoveBot(env, robot, peaches_173, camera)
    donothing(env)
