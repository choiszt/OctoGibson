import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    alarm = registry(env, "fire_alarm_88")
    ground = registry('ground')
