import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Unfold the rag.
    rag = registry(env, "rag_194")
    unfold(robot, rag)
    donothing(env)
