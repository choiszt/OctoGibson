import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Place the butter on the plate
    butter = registry(env,"butter_208")
    plate = registry(env,"plate_215")
    put_ontop(robot, butter, plate)
    donothing(env)
