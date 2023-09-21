import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the pocketknife into the wicker basket.
    put_inside(robot, pocketknife_278, wicker_basket_276)
    donothing(env)
