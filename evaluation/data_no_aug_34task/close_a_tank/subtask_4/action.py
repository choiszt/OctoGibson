import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    fuel_taker_188 = registry(env, "tank_88")
    EasyGrasp(robot, 'fuel-taker-188')
    donothing(env)
