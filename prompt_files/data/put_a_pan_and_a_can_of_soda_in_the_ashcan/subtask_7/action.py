import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Explore the environment to find the pan
    # As there is no specific function to explore the environment, we will move the robot to different objects in the environment to find the pan.
    notepad_86 = registry(env,"notepad_86")
    MoveBot(env, robot, notepad_86, camera)
    donothing(env)
