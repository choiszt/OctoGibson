import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move the robot to the basket (wicker_basket_88)
    wicker_basket_88 = registry(env,"wicker_basket_88")
    MoveBot(env, robot, wicker_basket_88, camera)
    donothing(env)
