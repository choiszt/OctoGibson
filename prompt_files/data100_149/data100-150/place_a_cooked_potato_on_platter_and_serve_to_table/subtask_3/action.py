import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the potato from the fridge.
    potato = registry(env, "potato_89")
    EasyGrasp(robot, potato)
    donothing(env)
