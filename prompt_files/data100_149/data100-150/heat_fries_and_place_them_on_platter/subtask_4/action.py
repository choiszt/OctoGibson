import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the fries inside the microwave
    microwave = registry(env, "microwave_bfbeeb_0")
    fries = registry(env, "french_fries_88")
    put_inside(robot, fries, microwave)
    donothing(env)
