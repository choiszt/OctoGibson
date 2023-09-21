import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take out the rag from the clothes dryer.
    rag = registry(env, "rag_194")
    clothes_dryer = registry(env, "clothes_dryer_zlmnfg_0")
    open(robot, clothes_dryer)
    donothing(env)
    EasyGrasp(robot, rag)
    donothing(env)
    close(robot, clothes_dryer)
    donothing(env)
