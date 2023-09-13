import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Pick up the croissant from the breakfast table
    croissant = registry(env, "croissant_283")
    EasyGrasp(robot, croissant)
    donothing(env)
