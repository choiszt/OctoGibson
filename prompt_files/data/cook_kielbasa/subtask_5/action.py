import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: If the kielbasa is in the fridge, grasp it
    kielbasa = registry(env, "kielbasa_1234")
    EasyGrasp(robot, kielbasa)
    donothing(env)
