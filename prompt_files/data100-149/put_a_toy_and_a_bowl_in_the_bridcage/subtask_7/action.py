import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move the robot to the bowl_189
    bowl_189 = registry(env,"bowl_189")
    MoveBot(env, robot, bowl_189, camera)
    donothing(env)
