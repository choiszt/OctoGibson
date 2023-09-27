import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    alarm_condition_1 = ['robot', 'nextto', 'alarm', 'condition', '1']
    MoveBot(env, robot, robot, camera)
    donothing(env)
