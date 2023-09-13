import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the breakfast table where the chopping board is located.
    breakfast_table = registry(env, "breakfast_table_idnnmz_0")
    MoveBot(env, robot, breakfast_table, camera)
    donothing(env)
