import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, robot, env, camera):
    unfold(robot, env, camera)
    donothing(env)
