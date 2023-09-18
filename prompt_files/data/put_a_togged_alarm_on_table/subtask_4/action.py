import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the fire alarm on the breakfast table
    fire_alarm_88 = registry(env, "fire_alarm_88")
    breakfast_table_uhrsex_0 = registry(env, "breakfast_table_uhrsex_0")
    put_ontop(robot, fire_alarm_88, breakfast_table_uhrsex_0)
    donothing(env)
