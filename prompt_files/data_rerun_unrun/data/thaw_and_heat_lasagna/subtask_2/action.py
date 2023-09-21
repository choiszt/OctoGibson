import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the lasagna from the fridge
    lasagna_85 = registry(env,"lasagna_85")
    EasyGrasp(robot, lasagna_85)
    donothing(env)
