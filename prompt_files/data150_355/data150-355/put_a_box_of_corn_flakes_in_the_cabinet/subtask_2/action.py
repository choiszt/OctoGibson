import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the box of corn flakes.
    box_of_corn_flakes_87 = registry(env,"box_of_corn_flakes_87")
    EasyGrasp(robot, box_of_corn_flakes_87)
    donothing(env)
