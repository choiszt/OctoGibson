import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    bottom_cupboard = registry(env, "bottom_cabinet_qacthv_0")
    open(robot, (bottom_cupboard - camera))
    donothing(env)
