import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the chicken
    chicken_278 = registry(env,"chicken_278")
    EasyGrasp(robot, chicken_278)
    donothing(env)
