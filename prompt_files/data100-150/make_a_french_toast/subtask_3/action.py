import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the french toast from the oven
    french_toast = registry(env, "french_toast_188")
    EasyGrasp(robot, french_toast)
    donothing(env)
