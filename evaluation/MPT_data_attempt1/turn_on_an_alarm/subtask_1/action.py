import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *


def act(robot, env, camera):
    fire_alert_142 = registry(env, "fire_alarm_88")
    MoveBot(env, robot, fire_alert_142, camera)
    donothing(env)
