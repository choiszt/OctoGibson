import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the cup of yogurt
    cup_of_yogurt_88 = registry(env,"cup_of_yogurt_88")
    EasyGrasp(robot, cup_of_yogurt_88)
    donothing(env)
