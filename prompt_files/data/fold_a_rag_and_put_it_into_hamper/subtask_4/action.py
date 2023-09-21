import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Fold the rag
    rag = registry(env, "rag_194")
    fold(robot, rag)
    donothing(env)
