import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    cabinerask_98 = registry(env, "top_cabinet_dmwxyl_0")
    open(robot, cabinerask_98)
    donothing(env)
