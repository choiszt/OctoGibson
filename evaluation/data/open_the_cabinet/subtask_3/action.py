import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env):
    cabinedask_88 = registry(env, "bottom_cabinet_no_top_qudfwe_0")
    registry(env, cabinedask_88)
    donothing(env)
    EasyGrasp(robot, env)
