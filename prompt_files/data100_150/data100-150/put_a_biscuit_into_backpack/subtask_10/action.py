import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 2: Open the backpack.
  backpack = registry(env, "backpack_277")
  donothing(env)
  open(robot, backpack)
  donothing(env)
