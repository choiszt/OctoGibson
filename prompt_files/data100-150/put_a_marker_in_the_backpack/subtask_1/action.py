import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the marker and the backpack
    marker_82 = registry(env,"marker_82")
    backpack_88 = registry(env,"backpack_88")
    # Subtask 2: Grasp the marker
    EasyGrasp(robot, marker_82)
    donothing(env)
