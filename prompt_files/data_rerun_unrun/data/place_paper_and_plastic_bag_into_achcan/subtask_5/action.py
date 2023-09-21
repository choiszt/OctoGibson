import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move the robot to the plastic bag
    plastic_bag_275 = registry(env,"plastic_bag_275")
    MoveBot(env, robot, plastic_bag_275, camera)
    donothing(env)
