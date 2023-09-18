import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the ashcan
    ashcan = registry(env,"trash_can_284")
    MoveBot(env, robot, ashcan, camera)
    donothing(env)
