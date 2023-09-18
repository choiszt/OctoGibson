import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the paraffin wax from the grocery shelf
    paraffin_wax = registry(env, "paraffin_wax_142")
    EasyGrasp(robot, paraffin_wax)
    donothing(env)
