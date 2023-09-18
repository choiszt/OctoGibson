import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 2: Grasp the pack of pasta.
  pack_of_pasta_146 = registry(env,"pack_of_pasta_146")
  EasyGrasp(robot, pack_of_pasta_146)
  donothing(env)
