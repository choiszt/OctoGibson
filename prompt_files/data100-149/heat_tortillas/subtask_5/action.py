import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the tortilla on the plate
    plate_150 = registry(env,"plate_150")
    tortilla_153 = registry(env,"tortilla_153")
    put_ontop(robot, tortilla_153, plate_150)
    donothing(env)
