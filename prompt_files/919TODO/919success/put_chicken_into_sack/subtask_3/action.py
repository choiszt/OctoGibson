import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the paper bag
    paper_bag_276 = registry(env,"paper_bag_276")
    MoveBot(env, robot, paper_bag_276, camera)
    donothing(env)
