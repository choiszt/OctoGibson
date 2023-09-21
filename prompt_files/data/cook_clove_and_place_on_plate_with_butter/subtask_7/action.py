import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the garlic clove on the stove
    stove_igwqpj_0 = registry(env,"stove_igwqpj_0")
    put_ontop(robot, garlic_clove_209, stove_igwqpj_0)
    donothing(env)
