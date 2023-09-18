import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 1: Register the trash can, the valentine wreath, and the leaf.
  trash_can_276 = registry(env, "trash_can_276")
  valentine_wreath_280 = registry(env, "valentine_wreath_280")
  leaf_277 = registry(env, "leaf_277")
  
  # Subtask 2: Move the robot to the valentine wreath.
  MoveBot(env, robot, valentine_wreath_280, camera)
  donothing(env)
