import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the soccer ball in the carton
    carton_87 = registry(env,"carton_87")
    soccer_ball_89 = registry(env,"soccer_ball_89")
    put_inside(robot, soccer_ball_89, carton_87)
    donothing(env)
