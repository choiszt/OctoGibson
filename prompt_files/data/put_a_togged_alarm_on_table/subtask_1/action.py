import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the fire alarm and the breakfast table
    fire_alarm_88 = registry(env, "fire_alarm_88")
    breakfast_table_uhrsex_0 = registry(env, "breakfast_table_uhrsex_0")
    
    # Subtask 2: Toggle on the fire alarm
    toggle_on(robot, fire_alarm_88)
    donothing(env)
