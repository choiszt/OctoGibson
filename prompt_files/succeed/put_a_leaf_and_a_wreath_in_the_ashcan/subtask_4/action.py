import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 5: Grasp the leaf.
  leaf_277 = registry(env, "leaf_277")
  EasyGrasp(robot, leaf_277)
  donothing(env)
