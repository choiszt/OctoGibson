import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the money on the cash register
    cash_register_142 = registry(env,"cash_register_142")
    money_146 = registry(env,"money_146")
    put_ontop(robot, money_146, cash_register_142)
    donothing(env)
