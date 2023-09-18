import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the box of lasagna.
    box_of_lasagna_85 = registry(env,"box_of_lasagna_85")
    EasyGrasp(robot, box_of_lasagna_85)
    donothing(env)
