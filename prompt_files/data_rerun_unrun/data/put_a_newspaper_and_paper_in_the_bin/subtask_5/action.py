import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move the robot to the notepad
    notepad_172 = registry(env,"notepad_172")
    coffee_table_gcollb_0 = registry(env,"coffee_table_gcollb_0")
    MoveBot(env, robot, coffee_table_gcollb_0, camera)
    donothing(env)
