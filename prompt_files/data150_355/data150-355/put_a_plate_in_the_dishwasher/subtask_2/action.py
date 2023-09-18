import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the plate
    plate_85 = registry(env,"plate_85")
    EasyGrasp(robot, plate_85)
    donothing(env)
