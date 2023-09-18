import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Grasp the plastic bag
    plastic_bag = registry(env, "plastic_bag_145")
    EasyGrasp(robot, plastic_bag)
    donothing(env)
