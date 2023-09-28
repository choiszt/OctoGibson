import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    money_142 = registry(env, ['money_143'])
    EasyGrasp(robot, money_142)
    donothing(env)
