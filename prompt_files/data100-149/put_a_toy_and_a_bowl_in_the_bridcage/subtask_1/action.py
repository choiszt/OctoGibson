import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the toy_figure_191
    toy_figure_191 = registry(env,"toy_figure_191")
    MoveBot(env, robot, toy_figure_191, camera)
    donothing(env)
