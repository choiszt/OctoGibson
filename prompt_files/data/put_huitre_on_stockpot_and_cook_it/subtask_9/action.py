import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Cook the oyster
    stove = registry(env, "stove_igwqpj_0")
    cook(robot, stove)
    donothing(env)
