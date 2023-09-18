import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move to the sack (paper_bag_85)
    sack = registry(env, "paper_bag_85")
    MoveBot(env, robot, sack, camera)
    donothing(env)
