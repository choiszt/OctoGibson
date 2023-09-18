import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the bottle of wine on the checkout counter.
    bottle_of_wine = registry(env, "bottle_of_wine_143")
    checkout_counter = registry(env, "checkout_counter_sckdal_0")
    put_ontop(robot, bottle_of_wine, checkout_counter)
    donothing(env)
