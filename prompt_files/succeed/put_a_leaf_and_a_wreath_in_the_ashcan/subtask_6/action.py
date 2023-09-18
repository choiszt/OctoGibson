import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 7: Put the valentine wreath in the trash can.
  valentine_wreath_280 = registry(env, "valentine_wreath_280")
  trash_can_276 = registry(env, "trash_can_276")
  put_inside(robot, valentine_wreath_280, trash_can_276)
  donothing(env)
