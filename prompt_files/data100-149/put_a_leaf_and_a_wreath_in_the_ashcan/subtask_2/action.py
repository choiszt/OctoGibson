import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 3: Grasp the valentine wreath.
  valentine_wreath_280 = registry(env, "valentine_wreath_280")
  EasyGrasp(robot, valentine_wreath_280)
  donothing(env)
