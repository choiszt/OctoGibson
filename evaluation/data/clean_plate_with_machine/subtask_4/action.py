import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    plate_170 = registry(env, "plate_170")
    machine_172 = registry(env, "tablefork_172")
    unfold(robot, plate_170, machine_172)
    donothing(env)
