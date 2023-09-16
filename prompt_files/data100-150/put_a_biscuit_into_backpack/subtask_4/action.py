import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 3: Find the biscuit inside the backpack.
  biscuit = registry(env, "biscuit")
  donothing(env)
