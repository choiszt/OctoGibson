import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Freeze the strawberry
    strawberry = registry(env, "strawberry_91")
    freeze(robot, strawberry)
    donothing(env)
