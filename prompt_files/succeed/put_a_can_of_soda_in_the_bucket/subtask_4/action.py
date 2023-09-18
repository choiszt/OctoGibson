import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the can of soda
    can_of_soda_183 = registry(env,"can_of_soda_183")
    EasyGrasp(robot, can_of_soda_183)
    donothing(env)
