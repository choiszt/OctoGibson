import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Open the microwave
    microwave = registry(env,"microwave_bfbeeb_0")
    open(robot, microwave)
    donothing(env)
