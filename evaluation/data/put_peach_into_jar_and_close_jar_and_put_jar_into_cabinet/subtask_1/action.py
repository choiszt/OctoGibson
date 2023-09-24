import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    jar_of_peash_173 = registry(env, "peach_173")
    MoveBot(env, robot, jar_of_peash_173, camera)
    donothing(env)
