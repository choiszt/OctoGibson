import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Put the hamburger in the microwave
    microwave = registry(env,"microwave_bfbeeb_0")
    hamburger = registry(env,"hamburger_85")
    put_inside(robot, hamburger, microwave)
    donothing(env)
