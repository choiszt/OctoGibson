import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the plastic bag into the trash can
    trash_can_279 = registry(env,"trash_can_279")
    plastic_bag_275 = registry(env,"plastic_bag_275")
    put_inside(robot, plastic_bag_275, trash_can_279)
    donothing(env)
