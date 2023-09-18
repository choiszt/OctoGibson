import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the strawberries in the bowl
    strawberries = registry(env, "strawberries_86")
    bowl = registry(env, "bowl_85")
    put_ontop(robot, strawberries, bowl)
    donothing(env)
