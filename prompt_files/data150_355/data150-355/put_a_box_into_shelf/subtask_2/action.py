import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 1: Move the robot to the suitcase_278
  suitcase_278 = registry(env,"suitcase_278")
  MoveBot(env, robot, suitcase_278, camera)
  donothing(env)
