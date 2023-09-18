import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 1: Find the toaster oven, wooden spoon, and cabinet in the environment.
  toaster_oven = registry(env, "toaster_oven")
  wooden_spoon = registry(env, "wooden_spoon")
  cabinet = registry(env, "cabinet")
