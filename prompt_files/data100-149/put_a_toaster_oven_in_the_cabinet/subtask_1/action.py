import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 1: Find the toaster oven.
  toaster_oven = registry(env, "toaster_oven")
