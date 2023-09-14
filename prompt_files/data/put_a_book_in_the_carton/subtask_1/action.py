import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the book
    book = registry(env, "hardback_188")
    MoveBot(env, robot, book, camera)
    donothing(env)
