import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the cheese tart on the plate
    cheese_tart = registry(env,"cheese_tart_85")
    plate = registry(env,"plate_87")
    put_ontop(robot, cheese_tart, plate)
    donothing(env)
