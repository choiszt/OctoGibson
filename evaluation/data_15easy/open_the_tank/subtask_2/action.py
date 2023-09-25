import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    wicker_wizard = registry(env, "bucket_89")
    EasyGrasp(robot, wicker_wizard)
    donothing(env)
