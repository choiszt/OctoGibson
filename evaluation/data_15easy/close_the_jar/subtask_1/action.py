import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    jar_jar_91 = registry(env, "jar_172")
    MoveBot(env, robot, jar_jar_91, camera)
    donothing(env)
