import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the oyster
    oyster = registry(env,"oyster_201")
    stove = registry(env,"stove_igwqpj_0")
    MoveBot(env, robot, oyster, camera)
    donothing(env)
