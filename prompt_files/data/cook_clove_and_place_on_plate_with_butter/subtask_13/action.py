import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move the robot to the stove
    stove = registry(env,"stove_igwqpj_0")
    MoveBot(env, robot, stove, camera)
    donothing(env)
