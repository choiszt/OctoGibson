import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Take the apple out of the bowl
    apple_87 = registry(env,"apple_87")
    bowl_88 = registry(env,"bowl_88")
    put_ontop(robot, apple_87, bowl_88)
    donothing(env)
