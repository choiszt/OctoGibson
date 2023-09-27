import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    beet3 = registry(env, "beet_277")
    EasyGrasp(robot, beet3)
    donothing(env)
