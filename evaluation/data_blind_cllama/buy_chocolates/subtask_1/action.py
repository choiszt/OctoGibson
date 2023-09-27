import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    fridge = registry(env, "swing_nppayh_0")
    open(robot, fridge)
    donothing(env)
