import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    money = (env, 'money_140,', 'money_-142,')
    EasyGrasp(robot, camera)
    donothing(env)
