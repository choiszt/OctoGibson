import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Heat the fries in the microwave
    microwave = registry(env, "microwave_bfbeeb_0")
    heat(robot, microwave)
    donothing(env)
