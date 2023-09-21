import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: If the rag is foldable, fold the rag.
    rag_194 = registry(env,"rag_194")
    for obj in env.get_observed_objects():
        if obj[0] == 'rag_194' and ('foldable', 1) in obj[1]:
            fold(robot, rag_194)
            donothing(env)
            break
