import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 1: Do nothing as the water bottle is already on the countertop.
  donothing(env)
