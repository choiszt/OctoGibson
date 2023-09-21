import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the carrot into the saucepot
    carrot = registry(env,"carrot_151")
    saucepot = registry(env,"saucepot_150")
    put_inside(robot, carrot, saucepot)
    donothing(env)
