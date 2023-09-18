import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the bottle of lotion
    bottle_of_lotion_195 = registry(env,"bottle_of_lotion_195")
    MoveBot(env, robot, bottle_of_lotion_195, camera)
    donothing(env)
