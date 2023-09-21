import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Find the quail inside the fridge
    quail = registry(env,"quail")
    # Subtask 4: Take out the quail from the fridge
    EasyGrasp(robot, quail)
    donothing(env)
