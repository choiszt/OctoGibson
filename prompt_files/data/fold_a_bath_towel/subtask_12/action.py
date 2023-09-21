import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Unfold the bath towel.
    bath_towel = registry(env,"bath_towel_192")
    unfold(robot, bath_towel)
    donothing(env)
