import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the coffee table where the cheese is located
    coffee_table_fqluyq_0 = registry(env,"coffee_table_fqluyq_0")
    MoveBot(env, robot, coffee_table_fqluyq_0, camera)
    donothing(env)
