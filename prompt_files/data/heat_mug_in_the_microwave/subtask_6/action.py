import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the mug inside the microwave
    mug = registry(env, "mug_188")
    microwave = registry(env, "microwave_bfbeeb_0")
    put_inside(robot, mug, microwave)
    donothing(env)
