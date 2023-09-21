import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp a bread slice from the bottom cabinet
    bread_slice = registry(env, "bread_slice_87")
    EasyGrasp(robot, bread_slice)
    donothing(env)
