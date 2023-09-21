import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the object 'rag_194'.
    rag_194 = registry(env,"rag_194")
    donothing(env)
