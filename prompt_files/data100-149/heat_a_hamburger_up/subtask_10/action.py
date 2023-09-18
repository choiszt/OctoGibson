import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 10: Toggle off the microwave after heating.
    microwave_bfbeeb_0 = registry(env,"microwave_bfbeeb_0")
    toggle_off(robot, microwave_bfbeeb_0)
    donothing(env)
