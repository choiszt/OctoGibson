import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the radio
    radio_34 = registry(env,"radio_34")
    MoveBot(env, robot, radio_34, camera)
    donothing(env)
