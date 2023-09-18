import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the bar soap back into the cabinet.
    top_cabinet_dmwxyl_2 = registry(env,"top_cabinet_dmwxyl_2")
    bar_soap_192 = registry(env,"bar_soap_192")
    put_inside(robot, bar_soap_192, top_cabinet_dmwxyl_2)
    donothing(env)
