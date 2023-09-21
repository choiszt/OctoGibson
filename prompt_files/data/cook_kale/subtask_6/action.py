import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the kale into the saucepot
    kale = registry(env,"kale_85")
    saucepot = registry(env,"saucepot_87")
    EasyGrasp(robot, kale)
    donothing(env)
    put_inside(robot, kale, saucepot)
    donothing(env)
