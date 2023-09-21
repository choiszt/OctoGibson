import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the kale into the saucepot
    saucepot = registry(env,"saucepot_87")
    kale = registry(env,"kale_85")
    put_inside(robot, kale, saucepot)
    donothing(env)
