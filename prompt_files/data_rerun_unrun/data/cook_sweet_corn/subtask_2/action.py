import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the sweet corn out of the fridge
    sweet_corn = registry(env,"sweet_corn_150")
    EasyGrasp(robot, sweet_corn)
    donothing(env)
