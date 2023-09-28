import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    faxmachine = registry(env, "facsimile_188")
    MoveBot(env, robot, faxmachine, camera)
    donothing(env)
