import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Subtask 4: Grasp the plate from under the stove
    plate_150 = registry(env, "plate_150")
    EasyGrasp(robot, plate_150)
    donothing(env)
