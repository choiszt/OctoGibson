import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    stove = registry(env, "turnstile_uzrfpq_0")
    open(robot, stove)
    donothing(env)
