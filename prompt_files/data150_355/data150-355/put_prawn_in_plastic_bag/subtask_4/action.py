import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the plastic bag
    plastic_bag_143 = registry(env,"plastic_bag_143")
    EasyGrasp(robot, plastic_bag_143)
    donothing(env)
