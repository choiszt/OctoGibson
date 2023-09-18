import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the bowl.
    bowl = registry(env, "bowl_190")
    EasyGrasp(robot, bowl)
    donothing(env)
