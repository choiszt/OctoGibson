import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the egg
    egg_92 = registry(env,"egg_92")
    MoveBot(env, robot, egg_92, camera)
    donothing(env)
