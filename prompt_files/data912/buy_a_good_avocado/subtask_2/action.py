import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Pay for the avocado
    money_143 = registry(env,"money_143")
    checkout_counter_sckdal_0 = registry(env,"checkout_counter_sckdal_0")
    EasyGrasp(robot, money_143)
    donothing(env)
    put_ontop(robot, money_143, checkout_counter_sckdal_0)
    donothing(env)
