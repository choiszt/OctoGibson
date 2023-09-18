import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the frozen meat on the plate
    pork_chop_188 = registry(env,"pork_chop_188")
    plate_191 = registry(env,"plate_191")
    put_ontop(robot, pork_chop_188, plate_191)
    donothing(env)
