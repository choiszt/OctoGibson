import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the egg
    egg_89 = registry(env,"egg_89")
    MoveBot(env, robot, egg_89, camera)
    donothing(env)
