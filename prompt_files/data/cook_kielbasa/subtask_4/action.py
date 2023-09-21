import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Check if the kielbasa is in the fridge
    fridge = registry(env, "fridge_xyejdx_0")
    kielbasa = registry(env, "kielbasa_1234")
    if kielbasa in fridge.get_contains():
        # Subtask 4: Grasp the kielbasa
        EasyGrasp(robot, kielbasa)
        donothing(env)
