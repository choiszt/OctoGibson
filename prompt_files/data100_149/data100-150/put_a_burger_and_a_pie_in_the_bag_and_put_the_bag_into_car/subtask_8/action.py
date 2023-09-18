import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Grasp the croissant
    croissant_282 = registry(env,"croissant_282")
    EasyGrasp(robot, croissant_282)
    donothing(env)
