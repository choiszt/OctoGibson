import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: If the bath towel is not foldable, unfold it.
    bath_towel = registry(env, "bath_towel_191")
    unfold(robot, bath_towel)
    donothing(env)
