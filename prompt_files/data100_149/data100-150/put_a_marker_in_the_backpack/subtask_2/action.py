import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the marker in the backpack
    marker_82 = registry(env,"marker_82")
    backpack_88 = registry(env,"backpack_88")
    put_inside(robot, marker_82, backpack_88)
    donothing(env)
