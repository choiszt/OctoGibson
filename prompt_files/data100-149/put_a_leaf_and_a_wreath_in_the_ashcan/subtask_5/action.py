import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
  # Subtask 6: Move the robot to the trash can.
  trash_can_276 = registry(env, "trash_can_276")
  MoveBot(env, robot, trash_can_276, camera)
  donothing(env)
