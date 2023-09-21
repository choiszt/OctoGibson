import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the fruitcake on the baking sheet
    baking_sheet_189 = registry(env,"baking_sheet_189")
    fruitcake_188 = registry(env,"fruitcake_188")
    put_ontop(robot, fruitcake_188, baking_sheet_189)
    donothing(env)
