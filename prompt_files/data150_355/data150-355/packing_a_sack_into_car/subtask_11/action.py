import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp the sack
    bap_280 = registry(env, "bap_280")
    EasyGrasp(robot, bap_280)
    donothing(env)
