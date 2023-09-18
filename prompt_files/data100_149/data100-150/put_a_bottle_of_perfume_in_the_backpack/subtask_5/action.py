import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the bottle of perfume in the backpack
    bottle_of_perfume_85 = registry(env,"bottle_of_perfume_85")
    backpack_82 = registry(env,"backpack_82")
    put_inside(robot, bottle_of_perfume_85, backpack_82)
    donothing(env)
