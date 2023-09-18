import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Heat the brisket
    brisket = registry(env,"brisket_189")
    heat(robot, brisket)
    donothing(env)
