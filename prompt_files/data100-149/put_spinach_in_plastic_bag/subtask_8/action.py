import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the spinach inside the plastic bag
    spinach = registry(env, "spinach_144")
    plastic_bag = registry(env, "plastic_bag_145")
    put_inside(robot, spinach, plastic_bag)
    donothing(env)
