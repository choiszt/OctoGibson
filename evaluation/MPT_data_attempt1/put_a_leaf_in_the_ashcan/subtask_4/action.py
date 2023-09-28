import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env):
    leaf_259 = registry(env, "leaf_277")
    EasyGrasp(robot, leaf_259)
    donothing(env)
