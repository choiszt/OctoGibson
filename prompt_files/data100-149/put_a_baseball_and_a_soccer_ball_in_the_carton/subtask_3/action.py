import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the baseball in the carton
    carton_87 = registry(env,"carton_87")
    baseball_88 = registry(env,"baseball_88")
    put_inside(robot, baseball_88, carton_87)
    donothing(env)
