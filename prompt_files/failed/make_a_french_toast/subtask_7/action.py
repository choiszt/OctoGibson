import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the french toast on the plate
    french_toast = registry(env, "french_toast_188")
    plate = registry(env, "plate_189")
    put_ontop(robot, french_toast, plate)
    donothing(env)
