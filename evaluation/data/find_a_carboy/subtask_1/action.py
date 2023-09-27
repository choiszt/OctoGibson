import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    bottom_cabinet = registry(env, "bottom_cabinet_no_top_qudfwe_0")
    open(robot, bottom_cabinet)
    donothing(env)
