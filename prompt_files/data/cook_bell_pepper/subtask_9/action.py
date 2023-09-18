import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the bell pepper.
    bell_pepper_123 = registry(env, "bell_pepper_123")
    EasyGrasp(robot, bell_pepper_123)
    donothing(env)
