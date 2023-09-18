import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 8: Put the leaf in the trash can.
  leaf_277 = registry(env, "leaf_277")
  trash_can_276 = registry(env, "trash_can_276")
  put_inside(robot, leaf_277, trash_can_276)
  donothing(env)
