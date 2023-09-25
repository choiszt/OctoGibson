import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    woredbaset = registry(env, "bucket_89")
    EasyGrasp(robot, woredbaset)
    donothing(env)
