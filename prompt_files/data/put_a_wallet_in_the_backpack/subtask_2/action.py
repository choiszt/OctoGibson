import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the wallet
    wallet_87 = registry(env,"wallet_87")
    EasyGrasp(robot, wallet_87)
    donothing(env)
