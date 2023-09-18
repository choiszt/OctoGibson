import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Move to the desk
    desk = registry(env, "desk_aduafr_0")
    MoveBot(env, robot, desk, camera)
    donothing(env)
