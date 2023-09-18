import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the cheese in the basket
    swiss_cheese_100 = registry(env,"swiss_cheese_100")
    wicker_basket_88 = registry(env,"wicker_basket_88")
    put_inside(robot, swiss_cheese_100, wicker_basket_88)
    donothing(env)
