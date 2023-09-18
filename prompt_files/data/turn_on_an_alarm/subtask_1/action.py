import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the fire_alarm_88
    fire_alarm_88 = registry(env,"fire_alarm_88")
    # Subtask 2: Toggle on the fire_alarm_88
    toggle_on(robot,fire_alarm_88)
    donothing(env)
