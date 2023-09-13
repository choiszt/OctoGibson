import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Pick up the suitcase from the breakfast table
    suitcase = registry(env, "suitcase_285")
    EasyGrasp(robot, suitcase)
    donothing(env)
