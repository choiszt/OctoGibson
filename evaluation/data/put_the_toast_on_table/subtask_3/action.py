import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    toast_150 = registry(env, "french_toast_188")
    EasyGrasp(robot, toast_150)
    donothing(env)
