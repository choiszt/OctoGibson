import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Heat the hamburger up in the microwave
    hamburger = registry(env,"hamburger_85")
    microwave = registry(env,"microwave_bfbeeb_0")
    heat(robot, hamburger)
    donothing(env)
