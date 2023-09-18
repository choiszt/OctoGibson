import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the plate into the dishwasher
    plate_191 = registry(env,"plate_191")
    dishwasher_znfvmj_0 = registry(env,"dishwasher_znfvmj_0")
    put_inside(robot, plate_191, dishwasher_znfvmj_0)
    donothing(env)
