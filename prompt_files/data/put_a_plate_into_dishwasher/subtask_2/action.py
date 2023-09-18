import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Move to the dishwasher
    dishwasher_znfvmj_0 = registry(env,"dishwasher_znfvmj_0")
    MoveBot(env, robot, dishwasher_znfvmj_0, camera)
    donothing(env)
