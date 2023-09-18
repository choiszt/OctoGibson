import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the lettuce in the plastic bag
    lettuce = registry(env, "lettuce_143")
    plastic_bag = registry(env, "plastic_bag_145")
    put_ontop(robot, lettuce, plastic_bag)
    donothing(env)
