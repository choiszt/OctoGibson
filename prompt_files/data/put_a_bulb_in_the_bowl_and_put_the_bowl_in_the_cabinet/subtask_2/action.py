import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the bulb
    daffodil_bulb_170 = registry(env,"daffodil_bulb_170")
    EasyGrasp(robot, daffodil_bulb_170)
    donothing(env)
