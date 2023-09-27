import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    carrot_151 = registry(env, "carrot_151")
    saucepot_170 = registry(env, "saucepot_150")
    unfold(robot, carrot_151, saucepot_170)
    donothing(env)
