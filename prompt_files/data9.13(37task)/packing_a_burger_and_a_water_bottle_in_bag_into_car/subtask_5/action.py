import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Grasp the suitcase
    EasyGrasp(robot, suitcase_286)
    donothing(env)
