import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Place the cooked prawn on the plate
    plate = registry(env,"plate_215")
    put_ontop(robot, "shrimp_201", plate)
    donothing(env)
