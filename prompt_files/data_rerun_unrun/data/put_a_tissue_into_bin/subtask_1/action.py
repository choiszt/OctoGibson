import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the tissue
    toilet_paper_278 = registry(env,"toilet_paper_278")
    MoveBot(env, robot, toilet_paper_278, camera)
    donothing(env)
