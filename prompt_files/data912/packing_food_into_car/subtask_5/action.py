import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the hamburger into the suitcase
    suitcase = registry(env, "suitcase_285")
    hamburger = registry(env, "hamburger_277")
    put_ontop(robot, hamburger, suitcase)
    donothing(env)
