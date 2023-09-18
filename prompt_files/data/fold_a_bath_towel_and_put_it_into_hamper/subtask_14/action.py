import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Fold the bath towel.
    bath_towel = registry(env, "bath_towel_191")
    fold(robot, bath_towel)
    donothing(env)
