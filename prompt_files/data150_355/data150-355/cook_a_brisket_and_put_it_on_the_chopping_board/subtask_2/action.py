import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the brisket out of the fridge
    brisket = registry(env,"brisket_189")
    EasyGrasp(robot, brisket)
    donothing(env)
