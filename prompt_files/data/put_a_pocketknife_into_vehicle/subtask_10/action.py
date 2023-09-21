import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Register the pocketknife.
    pocketknife_278 = registry(env,"pocketknife_278")
    # Subtask 5: Put the pocketknife into the wicker basket.
    put_inside(robot, pocketknife_278, wicker_basket_276)
    donothing(env)
