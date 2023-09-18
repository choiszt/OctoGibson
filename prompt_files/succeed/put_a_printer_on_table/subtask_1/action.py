import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the printer
    printer_188 = registry(env,"printer_188")
    EasyGrasp(robot, printer_188)
    donothing(env)
