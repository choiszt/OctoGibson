import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the wicker basket that contains the copper wire.
    wicker_basket_276 = registry(env, "wicker_basket_276")
    EasyGrasp(robot, wicker_basket_276)
    donothing(env)
