import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Find the wicker basket.
    wicker_basket_276 = registry(env, "wicker_basket_276")
    MoveBot(env, robot, wicker_basket_276, camera)
    donothing(env)
