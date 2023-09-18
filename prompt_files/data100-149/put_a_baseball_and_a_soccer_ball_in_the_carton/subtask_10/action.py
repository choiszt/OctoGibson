import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the soccer ball.
    soccer_ball_89 = registry(env,"soccer_ball_89")
    EasyGrasp(robot, soccer_ball_89)
    donothing(env)
