import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take out the asparagus from the fridge
    asparagus = registry(env, "asparagus_201")
    EasyGrasp(robot, asparagus)
    donothing(env)
