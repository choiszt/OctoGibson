import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    toggle_off(env, toggle_off(env, camera))
    EasyGrasp(robot, camera, env)
    donothing(env)
