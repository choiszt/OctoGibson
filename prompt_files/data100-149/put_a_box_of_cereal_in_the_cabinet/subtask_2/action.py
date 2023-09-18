import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the box of cereal.
    box_of_cereal_90 = registry(env,"box_of_cereal_90")
    EasyGrasp(robot, box_of_cereal_90)
    donothing(env)
