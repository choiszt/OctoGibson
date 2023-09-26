import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    machine_171 = registry(env, "plate_170")
    open(robot, machine_171)
    donothing(env)
