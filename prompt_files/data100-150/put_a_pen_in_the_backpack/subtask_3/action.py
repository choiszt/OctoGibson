import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 4: Put the pen in the backpack
  pen_83 = registry(env,"pen_83")
  backpack_82 = registry(env,"backpack_82")
  put_inside(robot, pen_83, backpack_82)
  donothing(env)
