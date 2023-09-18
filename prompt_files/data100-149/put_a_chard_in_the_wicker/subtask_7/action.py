import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the chard in the wicker basket
    chard_276 = registry(env,"chard_276")
    wicker_basket_278 = registry(env,"wicker_basket_278")
    put_inside(robot, chard_276, wicker_basket_278)
    donothing(env)
