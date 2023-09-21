import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the pack of pasta from the grocery shelf
    pack_of_pasta = registry(env, "pack_of_pasta_146")
    EasyGrasp(robot, pack_of_pasta)
    donothing(env)
