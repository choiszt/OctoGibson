import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the plastic bag from the top of the clothes dryer
    plastic_bag = registry(env, "plastic_bag_188")
    EasyGrasp(robot, plastic_bag)
    donothing(env)
