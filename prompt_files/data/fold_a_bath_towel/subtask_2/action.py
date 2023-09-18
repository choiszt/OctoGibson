import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp a bath towel from the clothes dryer
    bath_towel_191 = registry(env, "bath_towel_191")
    EasyGrasp(robot, bath_towel_191)
    donothing(env)
