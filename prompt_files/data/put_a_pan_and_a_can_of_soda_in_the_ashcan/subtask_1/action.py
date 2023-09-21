import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the trash can
    trash_can_85 = registry(env,"trash_can_85")
    MoveBot(env, robot, trash_can_85, camera)
    donothing(env)
    # Subtask 2: Register the trash can
    trash_can_85 = registry(env,"trash_can_85")
    donothing(env)
    # Subtask 3: Move the robot to the can of soda
    can_of_soda_89 = registry(env,"can_of_soda_89")
    MoveBot(env, robot, can_of_soda_89, camera)
    donothing(env)
    # Subtask 4: Register the can of soda
    can_of_soda_89 = registry(env,"can_of_soda_89")
    donothing(env)
