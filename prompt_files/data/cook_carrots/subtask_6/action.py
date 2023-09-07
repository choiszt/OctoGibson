import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Grasp the saucepot from the stove
    saucepot = registry(env,"saucepot_150")
    EasyGrasp(robot, saucepot)
    donothing(env)
