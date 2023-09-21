import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the lasagna from the oven
    lasagna = registry(env,"lasagna_85")
    EasyGrasp(robot, lasagna)
    donothing(env)
