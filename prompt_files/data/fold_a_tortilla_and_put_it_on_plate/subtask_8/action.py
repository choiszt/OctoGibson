import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Subtask 2: Unfold the tortilla
    tortilla_189 = registry(env, "tortilla_189")
    unfold(robot, tortilla_189)
    donothing(env)
