import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the plate
    plate_88 = registry(env,"plate_88")
    EasyGrasp(robot, plate_88)
    donothing(env)
