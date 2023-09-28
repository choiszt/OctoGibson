import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    leaf_285 = registry(env, "leaf_277")
    EasyGrasp(robot, env)
    donothing(env)
