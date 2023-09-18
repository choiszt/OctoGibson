import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the cookie
    spice_cookie_96 = registry(env,"spice_cookie_96")
    EasyGrasp(robot, spice_cookie_96)
    donothing(env)
