import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take a bath towel out of the clothes dryer.
    bath_towel = registry(env, "bath_towel_191")
    EasyGrasp(robot, bath_towel)
    donothing(env)
