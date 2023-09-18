import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the pack of ground beef
    pack_of_ground_beef = registry(env, "pack_of_ground_beef_87")
    EasyGrasp(robot, pack_of_ground_beef)
    donothing(env)
