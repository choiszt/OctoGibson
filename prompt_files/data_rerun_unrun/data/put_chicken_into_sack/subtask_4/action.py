import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the chicken into the sack
    chicken_278 = registry(env,"chicken_278")
    paper_bag_276 = registry(env,"paper_bag_276")
    put_inside(robot, chicken_278, paper_bag_276)
    donothing(env)
