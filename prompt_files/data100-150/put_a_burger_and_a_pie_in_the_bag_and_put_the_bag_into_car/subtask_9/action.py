import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 9: Put the croissant in the suitcase_285
    suitcase_285 = registry(env,"suitcase_285")
    put_inside(robot, croissant_282, suitcase_285)
    donothing(env)
