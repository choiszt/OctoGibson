import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp the carton of milk
    milk = registry(env,"carton_of_milk_86")
    EasyGrasp(robot, milk)
    donothing(env)
