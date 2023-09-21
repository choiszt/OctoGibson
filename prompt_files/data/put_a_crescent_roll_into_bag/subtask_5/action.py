import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the croissant into the suitcase
    croissant_283 = registry(env,"croissant_283")
    suitcase_285 = registry(env,"suitcase_285")
    put_inside(robot, croissant_283, suitcase_285)
    donothing(env)
