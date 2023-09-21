import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the rag out of the clothes dryer
    rag_194 = registry(env,"rag_194")
    EasyGrasp(robot, rag_194)
    donothing(env)
