import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 1: Move the robot to the wrapping paper.
  wrapping_paper_174 = registry(env,"wrapping_paper_174")
  MoveBot(env, robot, wrapping_paper_174, camera)
  donothing(env)
