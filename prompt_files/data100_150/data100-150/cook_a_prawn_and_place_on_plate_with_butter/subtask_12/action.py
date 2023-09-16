import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Defrost the prawn
    heat(robot, shrimp_201)
    donothing(env)
