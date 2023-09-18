import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the newspaper
    newspaper_171 = registry(env,"newspaper_171")
    EasyGrasp(robot, newspaper_171)
    donothing(env)
