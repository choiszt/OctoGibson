import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Take the rag out of the clothes dryer.
    rag = registry(env, "rag_194")
    clothes_dryer = registry(env, "clothes_dryer_zlmnfg_0")
    put_ontop(robot, rag, clothes_dryer)
    donothing(env)
