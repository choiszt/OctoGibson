import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the water bottle into the suitcase
    suitcase_286 = registry(env,"suitcase_286")
    water_bottle_284 = registry(env,"water_bottle_284")
    put_inside(robot, water_bottle_284, suitcase_286)
    donothing(env)
