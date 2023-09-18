import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the apple
    apple_193 = registry(env,"apple_193")
    EasyGrasp(robot, apple_193)
    donothing(env)
