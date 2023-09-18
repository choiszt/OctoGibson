import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the ice_bucket_285 and walnut_282
    ice_bucket_285 = registry(env,"ice_bucket_285")
    walnut_282 = registry(env,"walnut_282")
    
    # Subtask 2: Grasp the ice_bucket_285
    EasyGrasp(robot, ice_bucket_285)
    donothing(env)
