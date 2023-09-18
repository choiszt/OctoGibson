import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the suitcase down
    suitcase_276 = registry(env,"suitcase_276")
    driveway_aipswu_0 = registry(env,"driveway_aipswu_0")
    put_ontop(robot, suitcase_276, driveway_aipswu_0)
    donothing(env)
