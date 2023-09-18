import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move to the pitcher
    pitcher = registry(env, "jug_87")
    MoveBot(env, robot, pitcher, camera)
    donothing(env)
