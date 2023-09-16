import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the suitcase
    suitcase_276 = registry(env,"suitcase_276")
    EasyGrasp(robot, suitcase_276)
    donothing(env)
