import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Freeze the cheese tart.
    cheese_tart_85 = registry(env, "cheese_tart_85")
    freeze(robot, cheese_tart_85)
    donothing(env)
