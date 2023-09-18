import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the wallet and the backpack
    wallet_87 = registry(env,"wallet_87")
    backpack_82 = registry(env,"backpack_82")
    # Subtask 2: Grasp the wallet
    EasyGrasp(robot, wallet_87)
    donothing(env)
