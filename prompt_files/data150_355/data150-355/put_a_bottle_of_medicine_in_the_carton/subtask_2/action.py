import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the bottle of medicine
    bottle_of_medicine_194 = registry(env,"bottle_of_medicine_194")
    EasyGrasp(robot, bottle_of_medicine_194)
    donothing(env)
