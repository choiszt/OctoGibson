import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 2: Open the backpack
  open(robot, backpack_82)
  donothing(env)
