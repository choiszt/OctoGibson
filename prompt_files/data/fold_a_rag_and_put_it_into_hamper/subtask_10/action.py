import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the rag and the hamper
    rag_194 = registry(env,"rag_194")
    hamper_188 = registry(env,"hamper_188")
