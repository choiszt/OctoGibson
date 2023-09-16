import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Open the suitcase
    suitcase_279 = registry(env,"suitcase_279")
    open(robot, suitcase_279)
    donothing(env)
