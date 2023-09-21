import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the rag from the hamper
    rag = registry(env, "rag_194")
    EasyGrasp(robot, rag)
    donothing(env)
