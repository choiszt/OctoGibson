import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Pick up the hamburger from the breakfast table
    hamburger = registry(env, "hamburger_277")
    EasyGrasp(robot, hamburger)
    donothing(env)
