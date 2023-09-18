import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the chard
    chard_276 = registry(env,"chard_276")
    MoveBot(env, robot, chard_276, camera)
    donothing(env)
