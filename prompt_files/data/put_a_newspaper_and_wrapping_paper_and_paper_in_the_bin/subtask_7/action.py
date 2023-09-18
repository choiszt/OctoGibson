import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 7: Move the robot to the recycling bin.
  recycling_bin_170 = registry(env,"recycling_bin_170")
  MoveBot(env, robot, recycling_bin_170, camera)
  donothing(env)
