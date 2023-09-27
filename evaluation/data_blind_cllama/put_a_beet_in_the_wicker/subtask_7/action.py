import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    beet = registry(env, "beet_277")
    unfold(robot, beet)
    donothing(env)
