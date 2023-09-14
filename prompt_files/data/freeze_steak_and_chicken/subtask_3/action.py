import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take out the chicken
    chicken = registry(env, "chicken_176")
    EasyGrasp(robot, chicken)
    donothing(env)
