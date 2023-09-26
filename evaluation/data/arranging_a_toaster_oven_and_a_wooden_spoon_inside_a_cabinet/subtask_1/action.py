import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    toasteroven_188 = registry(env, "toaster_oven_170")
    MoveBot(env, robot, toasteroven_188, camera)
    donothing(env)
