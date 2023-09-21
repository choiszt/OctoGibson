import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Cook the garlic clove on the stove
    garlic_clove_209 = registry(env,"garlic_clove_209")
    stove_igwqpj_0 = registry(env,"stove_igwqpj_0")
    cook(robot, garlic_clove_209)
    donothing(env)
