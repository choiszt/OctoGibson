import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the vodka
    vodka = registry(env, "bottle_of_vodka_144")
    EasyGrasp(robot, vodka)
    donothing(env)
