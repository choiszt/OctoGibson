import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the plate inside the dishwasher
    plate_85 = registry(env,"plate_85")
    dishwasher_dngvvi_0 = registry(env,"dishwasher_dngvvi_0")
    put_inside(robot, plate_85, dishwasher_dngvvi_0)
    donothing(env)
