import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Check if the towel is hidden inside the cabinet by taking out the bar soap.
    bar_soap_192 = registry(env,"bar_soap_192")
    EasyGrasp(robot, bar_soap_192)
    donothing(env)
