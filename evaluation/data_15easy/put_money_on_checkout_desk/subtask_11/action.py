import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    money = (env, 'money-142,money-143')
    EasyGrasp(robot, camera)
    donothing(env)
