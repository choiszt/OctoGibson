import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Cook the prawn on the stove
    shrimp = registry(env,"shrimp_201")
    stove = registry(env,"stove_igwqpj_0")
    cook(robot, shrimp)
    donothing(env)
