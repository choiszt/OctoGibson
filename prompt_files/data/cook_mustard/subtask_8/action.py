import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Put the saucepan on the stove
    stove_igwqpj_0 = registry(env,"stove_igwqpj_0")
    saucepan_205 = registry(env,"saucepan_205")
    put_ontop(robot, saucepan_205, stove_igwqpj_0)
    donothing(env)
