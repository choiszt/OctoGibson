import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Cook the duck
    duck = registry(env,"duck_171")
    cook(robot, duck)
    donothing(env)
