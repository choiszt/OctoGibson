import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the rag back into the hamper
    rag = registry(env, "rag_194")
    hamper = registry(env, "hamper_188")
    put_ontop(robot, rag, hamper)
    donothing(env)
