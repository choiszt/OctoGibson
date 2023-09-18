import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 4: Put the wrapping paper in the recycling bin.
  wrapping_paper_174 = registry(env,"wrapping_paper_174")
  recycling_bin_170 = registry(env,"recycling_bin_170")
  put_inside(robot, wrapping_paper_174, recycling_bin_170)
  donothing(env)
