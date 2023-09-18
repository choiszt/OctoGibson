import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take out the rag from the cabinet
    rag = registry(env, "rag_89")
    EasyGrasp(robot, rag)
    donothing(env)
