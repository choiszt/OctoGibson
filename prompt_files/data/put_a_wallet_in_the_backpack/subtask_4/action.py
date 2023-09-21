import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the wallet inside the backpack
    wallet_87 = registry(env,"wallet_87")
    backpack_82 = registry(env,"backpack_82")
    put_inside(robot, wallet_87, backpack_82)
    donothing(env)
