import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move to the notebook
    notebook_148 = registry(env,"notebook_148")
    MoveBot(env, robot, notebook_148, camera)
    donothing(env)
