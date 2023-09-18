import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 9: Move the robot to the stove
    stove_igwqpj_0 = registry(env,"stove_igwqpj_0")
    MoveBot(env, robot, stove_igwqpj_0, camera)
    donothing(env)
