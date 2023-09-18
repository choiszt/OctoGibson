import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take out the fries and burger from the fridge
    french_fries = registry(env, "french_fries_88")
    hamburger = registry(env, "hamburger_85")
    EasyGrasp(robot, french_fries)
    donothing(env)
    EasyGrasp(robot, hamburger)
    donothing(env)
