import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the copper wire into the wicker_basket_276
    copper_wire_282 = registry(env, "copper_wire_282")
    wicker_basket_276 = registry(env, "wicker_basket_276")
    put_inside(robot, copper_wire_282, wicker_basket_276)
    donothing(env)
