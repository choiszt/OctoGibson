import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Cook the garlic clove
    garlic_clove_209 = registry(env,"garlic_clove_209")
    cook(robot, garlic_clove_209)
    donothing(env)
