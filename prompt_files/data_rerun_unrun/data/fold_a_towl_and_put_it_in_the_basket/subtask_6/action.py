import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Unfold the bath_towel_85.
    bath_towel_85 = registry(env,"bath_towel_85")
    unfold(robot, bath_towel_85)
    donothing(env)
