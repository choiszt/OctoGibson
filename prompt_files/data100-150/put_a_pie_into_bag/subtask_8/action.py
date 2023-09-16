import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the cheese_tart_280 into the suitcase_285
    cheese_tart_280 = registry(env,"cheese_tart_280")
    suitcase_285 = registry(env,"suitcase_285")
    put_inside(robot, cheese_tart_280, suitcase_285)
    donothing(env)
