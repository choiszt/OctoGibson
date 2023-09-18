import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Move to the front of the towel.
    paper_towel_193 = registry(env,"paper_towel_193")
    MoveBot(env, robot, paper_towel_193, camera)
    donothing(env)
