import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Put the cheese tart into the suitcase
    suitcase = registry(env, "suitcase_285")
    cheese_tart = registry(env, "cheese_tart_280")
    put_inside(robot, cheese_tart, suitcase)
    donothing(env)
