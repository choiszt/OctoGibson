import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Pick up the plate
    plate = registry(env,"plate_87")
    EasyGrasp(robot, plate)
    donothing(env)
