import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take out the garlic clove
    garlic_clove = registry(env,"garlic_clove_209")
    EasyGrasp(robot, garlic_clove)
    donothing(env)
