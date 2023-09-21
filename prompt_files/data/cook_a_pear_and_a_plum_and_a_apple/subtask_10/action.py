import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Grasp the apple from the bowl
    apple_87 = registry(env,"apple_87")
    EasyGrasp(robot, apple_87)
    donothing(env)
