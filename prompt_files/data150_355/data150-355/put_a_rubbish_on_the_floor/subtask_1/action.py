import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 1: Register the bag of rubbish
  bag_of_rubbish_276 = registry(env,"bag_of_rubbish_276")
  
  # Subtask 2: Grasp the bag of rubbish
  EasyGrasp(robot, bag_of_rubbish_276)
  donothing(env)
