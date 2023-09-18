import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 8: Put the newspaper in the recycling bin.
  newspaper_171 = registry(env,"newspaper_171")
  recycling_bin_170 = registry(env,"recycling_bin_170")
  put_inside(robot, newspaper_171, recycling_bin_170)
  donothing(env)
