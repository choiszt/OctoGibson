import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 3: Put the box of candy in the backpack
  put_inside(robot, box_of_candy_89, backpack_82)
  donothing(env)
