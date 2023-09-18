import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the mug in the microwave
    microwave_bfbeeb_0 = registry(env,"microwave_bfbeeb_0")
    mug_188 = registry(env,"mug_188")
    put_inside(robot, mug_188, microwave_bfbeeb_0)
    donothing(env)
