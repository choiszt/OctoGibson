import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Pay for the avocado
    checkout_counter_sckdal_0 = registry(env,"checkout_counter_sckdal_0")
    money_143 = registry(env,"money_143")
    put_ontop(robot, money_143, checkout_counter_sckdal_0)
    donothing(env)
