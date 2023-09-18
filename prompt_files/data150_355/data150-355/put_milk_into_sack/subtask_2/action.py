import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the carton_of_milk_277
    carton_of_milk_277 = registry(env,"carton_of_milk_277")
    EasyGrasp(robot, carton_of_milk_277)
    donothing(env)
