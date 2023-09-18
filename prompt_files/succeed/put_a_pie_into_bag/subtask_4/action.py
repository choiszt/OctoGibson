import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the hamburger_276 into the suitcase_285
    hamburger_276 = registry(env,"hamburger_276")
    suitcase_285 = registry(env,"suitcase_285")
    put_inside(robot, hamburger_276, suitcase_285)
    donothing(env)
