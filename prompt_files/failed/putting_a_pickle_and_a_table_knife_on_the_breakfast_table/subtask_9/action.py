import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take the pickle out of the fridge
    pickle = registry(env, "pickle_88")
    EasyGrasp(robot, pickle)
    donothing(env)
