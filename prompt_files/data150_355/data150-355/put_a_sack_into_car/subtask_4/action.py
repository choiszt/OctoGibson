import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the sack (paper_bag_279) inside the car (car_276)
    paper_bag_279 = registry(env,"paper_bag_279")
    car_276 = registry(env,"car_276")
    put_inside(robot, paper_bag_279, car_276)
    donothing(env)
