import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Turn off the stove
    stove = registry(env,"stove_igwqpj_0")
    toggle_off(robot, stove)
    donothing(env)
