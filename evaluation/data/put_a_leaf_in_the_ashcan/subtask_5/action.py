import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    leaf_277 = registry(env, "leaf_277")
    trash_can_281 = registry(env, "trash_can_276")
    unfold(robot, leaf_277, trash_can_281)
    donothing(env)
