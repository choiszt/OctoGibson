import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Grasp the bowl_189
    bowl_189 = registry(env,"bowl_189")
    EasyGrasp(robot, bowl_189)
    donothing(env)
