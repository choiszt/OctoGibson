import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the plastic bag and the trash can.
    plastic_bag_275 = registry(env,"plastic_bag_275")
    trash_can_279 = registry(env,"trash_can_279")
