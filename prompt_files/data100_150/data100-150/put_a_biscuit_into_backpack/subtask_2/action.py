import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 1: Move to the backpack.
  backpack = registry(env, "backpack_277")
  MoveBot(env, robot, backpack, camera)
  donothing(env)
