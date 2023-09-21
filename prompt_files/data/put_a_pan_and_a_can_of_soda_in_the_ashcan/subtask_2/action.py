import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Grasp the can of soda
    can_of_soda_89 = registry(env,"can_of_soda_89")
    EasyGrasp(robot, can_of_soda_89)
    donothing(env)
