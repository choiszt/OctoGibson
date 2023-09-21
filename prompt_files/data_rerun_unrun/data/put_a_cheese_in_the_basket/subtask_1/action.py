import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the cheese
    swiss_cheese_100 = registry(env,"swiss_cheese_100")
    MoveBot(env, robot, swiss_cheese_100, camera)
    donothing(env)
