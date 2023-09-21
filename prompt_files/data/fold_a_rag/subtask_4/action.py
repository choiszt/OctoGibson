import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Check if the rag is foldable
    rag_194 = registry(env,"rag_194")
    if rag_194['foldable'] == 1:
        fold(robot, rag_194)
        donothing(env)
