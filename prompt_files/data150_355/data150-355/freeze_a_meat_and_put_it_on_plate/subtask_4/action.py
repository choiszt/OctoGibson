import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp a plate
    plate_191 = registry(env,"plate_191")
    EasyGrasp(robot, plate_191)
    donothing(env)
