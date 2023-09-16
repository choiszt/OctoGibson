import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the croissant_282 in the suitcase_285
    croissant_282 = registry(env,"croissant_282")
    suitcase_285 = registry(env,"suitcase_285")
    put_inside(robot, croissant_282, suitcase_285)
    donothing(env)
