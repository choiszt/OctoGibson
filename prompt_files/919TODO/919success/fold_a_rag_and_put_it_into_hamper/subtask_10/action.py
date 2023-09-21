import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the rag
    rag = registry(env, "rag_194")
    MoveBot(env, robot, rag, camera)
    donothing(env)
