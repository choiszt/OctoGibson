import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the french toast on the plate
    plate = registry(env, "plate_189")
    french_toast = registry(env, "french_toast_188")
    put_ontop(robot, french_toast, plate)
    donothing(env)
