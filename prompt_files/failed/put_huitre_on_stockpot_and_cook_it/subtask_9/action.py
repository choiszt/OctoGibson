import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the oyster on the stove
    oyster = registry(env,"oyster_201")
    stove = registry(env,"stove_igwqpj_0")
    put_ontop(robot, oyster, stove)
    donothing(env)
