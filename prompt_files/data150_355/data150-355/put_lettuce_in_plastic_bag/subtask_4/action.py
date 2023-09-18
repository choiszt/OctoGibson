import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the plastic bag
    plastic_bag = registry(env, "plastic_bag_145")
    MoveBot(env, robot, plastic_bag, camera)
    donothing(env)
