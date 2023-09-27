import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    bucket_275 = registry(env, "ice_bucket_170")
    EasyGrasp(robot, bucket_275)
    donothing(env)
