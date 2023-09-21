import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Pick up the stockpot
    stockpot = registry(env,"stockpot_155")
    EasyGrasp(robot, stockpot)
    donothing(env)
