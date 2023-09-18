import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the scrub brush
    scrub_brush_34 = registry(env,"scrub_brush_34")
    # Subtask 2: Grasp the scrub brush
    EasyGrasp(robot, scrub_brush_34)
    donothing(env)
