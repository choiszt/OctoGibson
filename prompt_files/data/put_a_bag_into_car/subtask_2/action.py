import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Open the suitcase
    suitcase_285 = registry(env,"suitcase_285")
    open(robot, suitcase_285)
    donothing(env)
