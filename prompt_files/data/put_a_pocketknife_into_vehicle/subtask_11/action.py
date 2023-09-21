import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Register the wicker basket.
    wicker_basket_276 = registry(env,"wicker_basket_276")
