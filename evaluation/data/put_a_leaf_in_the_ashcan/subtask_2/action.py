import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    leaf_276 = registry(env, "leaf_277")
    EasyGrasp(robot, leaf_276)
    donothing(env)
