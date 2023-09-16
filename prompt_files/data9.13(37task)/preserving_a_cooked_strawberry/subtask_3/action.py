import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Cook the strawberry
    strawberry_201 = registry(env,"strawberry_201")
    cook(robot, strawberry_201)
    donothing(env)
