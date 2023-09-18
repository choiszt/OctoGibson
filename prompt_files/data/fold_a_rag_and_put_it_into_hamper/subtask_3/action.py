import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the rag.
    rag = registry(env, "rag_194")
    EasyGrasp(robot, rag)
    donothing(env)
