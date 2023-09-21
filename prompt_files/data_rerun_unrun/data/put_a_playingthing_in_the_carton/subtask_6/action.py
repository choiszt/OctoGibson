import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp the teddy bear
    teddy_bear_88 = registry(env,"teddy_bear_88")
    EasyGrasp(robot, teddy_bear_88)
    donothing(env)
