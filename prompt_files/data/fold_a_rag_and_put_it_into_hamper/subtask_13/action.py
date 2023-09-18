import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Unfold the rag
    rag_194 = registry(env,"rag_194")
    unfold(robot, rag_194)
    donothing(env)
