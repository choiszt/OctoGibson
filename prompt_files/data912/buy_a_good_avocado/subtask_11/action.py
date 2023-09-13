import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Place the avocado on the checkout counter.
    checkout_counter_sckdal_0 = registry(env,"checkout_counter_sckdal_0")
    avocado_142 = registry(env,"avocado_142")
    put_ontop(robot, avocado_142, checkout_counter_sckdal_0)
    donothing(env)
