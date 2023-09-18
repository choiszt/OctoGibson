import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Find the sack and move the robot to it
    bap_280 = registry(env,"bap_280")
    MoveBot(env, robot, bap_280, camera)
    donothing(env)
