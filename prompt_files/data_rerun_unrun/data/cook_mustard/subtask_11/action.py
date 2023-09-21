import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 11: Toggle on the stove to cook the mustard leaf
    stove_igwqpj_0 = registry(env,"stove_igwqpj_0")
    toggle_on(robot, stove_igwqpj_0)
    donothing(env)
