import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 1: Register the pen and the backpack
  pen_83 = registry(env,"pen_83")
  backpack_82 = registry(env,"backpack_82")
  
  # Subtask 2: Grasp the pen
  EasyGrasp(robot, pen_83)
  donothing(env)
