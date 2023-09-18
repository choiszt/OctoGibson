import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the carton of orange juice
    carton_of_orange_juice_89 = registry(env,"carton_of_orange_juice_89")
    EasyGrasp(robot, carton_of_orange_juice_89)
    donothing(env)
