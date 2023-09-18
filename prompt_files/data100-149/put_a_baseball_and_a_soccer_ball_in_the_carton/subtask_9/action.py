import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the soccer ball.
    soccer_ball_89 = registry(env,"soccer_ball_89")
    MoveBot(env, robot, soccer_ball_89, camera)
    donothing(env)
