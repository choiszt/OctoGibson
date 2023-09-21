import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the oyster from the stove
    oyster = registry(env, "oyster_201")
    EasyGrasp(robot, oyster)
    donothing(env)
