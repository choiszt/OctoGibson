import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Cook the garlic clove
    stove = registry(env,"stove_igwqpj_0")
    MoveBot(env, robot, stove, camera)
    donothing(env)
    cook(robot, garlic_clove)
    donothing(env)
