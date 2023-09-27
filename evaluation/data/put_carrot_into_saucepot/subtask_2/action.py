import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    carrot_178 = registry(env, "carrot_151")
    EasyGrasp(robot, carrot_178)
    donothing(env)
