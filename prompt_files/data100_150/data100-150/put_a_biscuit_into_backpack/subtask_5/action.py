import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 3: Search for the biscuit in the environment.
  biscuit = registry(env, "biscuit")
  donothing(env)
