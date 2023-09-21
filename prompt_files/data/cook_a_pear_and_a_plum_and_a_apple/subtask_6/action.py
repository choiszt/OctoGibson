import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Find and grasp a bowl
    bowl_88 = registry(env,"bowl_88")
    EasyGrasp(robot, bowl_88)
    donothing(env)
