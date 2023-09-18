import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the can of soda in the ice bucket
    can_of_soda_183 = registry(env,"can_of_soda_183")
    ice_bucket_189 = registry(env,"ice_bucket_189")
    put_inside(robot, can_of_soda_183, ice_bucket_189)
    donothing(env)
