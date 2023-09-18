import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 2: Search for the biscuit in the environment.
  # Since the biscuit is not in the observed objects, it might be inside the backpack.
  # The backpack is already open, so we just need to check inside.
  backpack = registry(env, "backpack_277")
  donothing(env)
