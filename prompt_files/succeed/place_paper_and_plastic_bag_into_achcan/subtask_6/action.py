import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Grasp the plastic bag
    plastic_bag_275 = registry(env,"plastic_bag_275")
    EasyGrasp(robot, plastic_bag_275)
    donothing(env)
