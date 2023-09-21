import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Take a plate from the countertop
    plate = registry(env, "plate_190")
    EasyGrasp(robot, plate)
    donothing(env)
