import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the wax paper
    wax_paper_173 = registry(env,"wax_paper_173")
    coffee_table_gcollb_0 = registry(env,"coffee_table_gcollb_0")
    MoveBot(env, robot, coffee_table_gcollb_0, camera)
    donothing(env)
