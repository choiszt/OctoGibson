import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Defrost the chicken
    chicken = registry(env,"chicken_189")
    heat(robot, chicken)
    donothing(env)
