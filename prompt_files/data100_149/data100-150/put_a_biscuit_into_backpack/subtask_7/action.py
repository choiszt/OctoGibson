import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 3: Search for the biscuit in the environment.
  # Since the biscuit is not in the observed objects, it might be inside the backpack.
  # So we need to open the backpack and check inside.
  backpack = registry(env, "backpack_277")
  open(robot, backpack)
  donothing(env)
