import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Put the folded bath towel into the hamper.
    bath_towel = registry(env, "bath_towel_192")
    hamper = registry(env, "hamper_188")
    put_inside(robot, bath_towel, hamper)
    donothing(env)
