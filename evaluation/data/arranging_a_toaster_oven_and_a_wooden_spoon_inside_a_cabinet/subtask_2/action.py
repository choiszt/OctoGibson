import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env):
    toasterive = registry(env, "toaster_oven_170")
    EasyGrasp(robot, toasterive)
    donothing(env)
