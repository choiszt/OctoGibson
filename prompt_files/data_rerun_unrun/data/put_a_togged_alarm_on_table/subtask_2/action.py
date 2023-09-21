import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the fire alarm
    fire_alarm_88 = registry(env, "fire_alarm_88")
    EasyGrasp(robot, fire_alarm_88)
    donothing(env)
