import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Fold the bath towel
    bath_towel_191 = registry(env, "bath_towel_191")
    fold(robot, bath_towel_191)
    donothing(env)
