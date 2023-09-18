import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the bottle of wine from the grocery shelf.
    bottle_of_wine = registry(env, "bottle_of_wine_143")
    EasyGrasp(robot, bottle_of_wine)
    donothing(env)
