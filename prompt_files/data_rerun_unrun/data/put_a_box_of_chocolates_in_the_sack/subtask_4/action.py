import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the box of chocolates in the sack
    chocolates = registry(env, "box_of_chocolates_91")
    sack = registry(env, "paper_bag_85")
    put_inside(robot, chocolates, sack)
    donothing(env)
