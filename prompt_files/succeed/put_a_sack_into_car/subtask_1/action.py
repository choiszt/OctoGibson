import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the sack (paper_bag_279)
    paper_bag_279 = registry(env,"paper_bag_279")
    MoveBot(env, robot, paper_bag_279, camera)
    donothing(env)
