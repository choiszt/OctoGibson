import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the carton_of_milk_277 into the paper_bag_276
    carton_of_milk_277 = registry(env,"carton_of_milk_277")
    paper_bag_276 = registry(env,"paper_bag_276")
    put_inside(robot, carton_of_milk_277, paper_bag_276)
    donothing(env)
