import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Grasp the saucepan
    saucepan_205 = registry(env,"saucepan_205")
    EasyGrasp(robot, saucepan_205)
    donothing(env)
