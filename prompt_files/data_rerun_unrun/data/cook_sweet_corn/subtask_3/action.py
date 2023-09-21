import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the sweet corn into the stockpot
    stockpot = registry(env,"stockpot_155")
    sweet_corn = registry(env,"sweet_corn_150")
    put_inside(robot, sweet_corn, stockpot)
    donothing(env)
