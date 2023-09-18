import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the tomato
    tomato = registry(env, "beefsteak_tomato_90")
    EasyGrasp(robot, tomato)
    donothing(env)
