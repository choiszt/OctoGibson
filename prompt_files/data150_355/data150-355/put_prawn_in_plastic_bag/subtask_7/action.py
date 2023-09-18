import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the prawn in the plastic bag
    shrimp_145 = registry(env,"shrimp_145")
    plastic_bag_143 = registry(env,"plastic_bag_143")
    put_inside(robot, shrimp_145, plastic_bag_143)
    donothing(env)
