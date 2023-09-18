import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the folded bath towel into the hamper.
    bath_towel_192 = registry(env, "bath_towel_192")
    hamper_188 = registry(env, "hamper_188")
    put_ontop(robot, bath_towel_192, hamper_188)
    donothing(env)
