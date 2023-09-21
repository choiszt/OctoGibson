import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Find the kielbasa in the fridge
    kielbasa = registry(env, "kielbasa_1234")
    # Subtask 4: Grasp the kielbasa
    EasyGrasp(robot, kielbasa)
    donothing(env)
