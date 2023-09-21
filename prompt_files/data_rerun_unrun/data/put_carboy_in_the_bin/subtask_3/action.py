import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the reagent bottle (carboy)
    reagent_bottle = registry(env, "reagent_bottle_189")
    EasyGrasp(robot, reagent_bottle)
    donothing(env)
