import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Move to the ice bucket
    ice_bucket_189 = registry(env,"ice_bucket_189")
    MoveBot(env, robot, ice_bucket_189, camera)
    donothing(env)
