import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the newspaper
    newspaper = registry(env, "newspaper_89")
    EasyGrasp(robot, newspaper)
    donothing(env)
