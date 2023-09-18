import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Toggle on the microwave to heat the hamburger.
    microwave = registry(env, "microwave_bfbeeb_0")
    toggle_on(robot, microwave)
    donothing(env)
