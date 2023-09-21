import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Heat the hamburger up in the microwave
    microwave = registry(env,"microwave_bfbeeb_0")
    heat(robot, microwave)
    donothing(env)
